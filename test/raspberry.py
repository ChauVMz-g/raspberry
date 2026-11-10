import sys
from time import sleep

import paho.mqtt.client as mqtt
from grove.gpio import GPIO
from gpiozero import Buzzer
from numpy import interp
from seeed_dht import DHT

import RPi.GPIO as IO
IO.setwarnings(False)
IO.setmode(IO.BCM)

SENSOR_PIN = 5
LED_PIN = 16
SERVO_PIN = 12
BUZZER_PIN = 22

buzzer = Buzzer(BUZZER_PIN)

# --- CẤU HÌNH MQTT ---
CHANNEL_ID = "3570604"
CLIENT_ID = "GwsKIxkcJjwLJDQZIzo0HhI"
USERNAME = "GwsKIxkcJjwLJDQZIzo0HhI"
PASSWORD = "voRTtpGdrWyCAwVvFAj6W64W"
BROKER_HOST = "mqtt3.thingspeak.com"
PUBLISH_INTERVAL = 20

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, CLIENT_ID)
client.username_pw_set(username=USERNAME, password=PASSWORD)
client.connect(BROKER_HOST, 1883, 60)
client.loop_start()


def publish(temp, humid):
  topic = f"channels/{CHANNEL_ID}/publish"
  payload = f"field1={temp}&field2={humid}&status=OK"
  client.publish(topic, payload)


class GroveLED(GPIO):
  def __init__(self, pin):
    super(GroveLED, self).__init__(pin, GPIO.OUT)

  def on(self):
    self.write(1)

  def off(self):
    self.write(0)


class GroveServo:
  def __init__(self, channel):
    IO.setup(channel, IO.OUT)
    self.pwm = IO.PWM(channel, 50)
    self.pwm.start(2.5)

  def setAngle(self, angle):
    angle = max(min(angle, 180), 0)
    tmp = interp(angle, [0, 180], [25, 125])
    self.pwm.ChangeDutyCycle(round(tmp / 10.0, 1))

  def stop(self):
    self.pwm.stop()


def main():
  sensor = DHT("22", SENSOR_PIN)
  led = GroveLED(LED_PIN)
  servo = GroveServo(SERVO_PIN)

  timer_counter = 0
  is_beeping = False
  last_temp = 0.0
  last_humi = 0.0

  try:
    while True:
      humi, temp = sensor.read()

      if temp is not None and humi is not None:
        last_temp = round(temp,1)
        last_humi = round(humi,1)

      print(f"Nhiet do: {last_temp}°C, Do am: {last_humi}%")

      # 1. Điều khiển LED
      if last_temp > 25:
        led.on()
      elif last_temp < 26:
        led.off()

      # 2. Điều khiển Servo
      servo.setAngle(last_humi)

      # 3. ĐIỀU KHIỂN CÒI BẰNG GPIOZERO
      if last_temp > 40:
        if not is_beeping:
          buzzer.beep(on_time=1, off_time=2)  # Bắt đầu luồng beep ngầm
          is_beeping = True
      else:
        if is_beeping:
          buzzer.off()  # Tắt còi và dừng luồng beep
          is_beeping = False

      # 4. Gửi MQTT 20s/lần
      timer_counter += 1
      if timer_counter >= PUBLISH_INTERVAL:
        publish(temp=last_temp, humid=last_humi)
        timer_counter = 0

      sleep(1)

  except KeyboardInterrupt:
    print("\n[INFO] Đã dừng chương trình.")
  finally:
    led.off()
    buzzer.off()
    servo.stop()
    IO.cleanup()

    client.loop_stop()
    client.disconnect()
    sys.exit(0)


if __name__ == "__main__":
  main()