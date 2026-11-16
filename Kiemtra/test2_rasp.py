from time import sleep
from urllib import request, parse, error

from grove.grove_light_sensor_v1_2 import GroveLightSensor   #Cảm biến ánh sáng
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger #Cảm biến khoảng cách

from grove.display.jhd1802 import JHD1802 #Hiển thị lên LCD

from gpiozero import LED 
from grove.grove_buzzer import GroveBuzzer

LIGHT_PIN = "0"
ULTRASONIC_PIN = "5"

LED_PIN = "16"
BUZZER_PIN = "12"

BASE_URL = "https://api.thingspeak.com"
API_KEY_WRITE = "KG8ED62ME1SB70C7"

def thingspeak_write(fields):
    body = parse.urlencode({f"field{k}": v for k, v in fields.items()}).encode()
    req = request.Request(f"{BASE_URL}/update", data=body, method="POST")
    req.add_header("Content-Type", "application/x-www-form-urlencoded")
    req.add_header("X-THINGSPEAKAPIKEY", API_KEY_WRITE)
    with request.urlopen(req, timeout=10) as r:
        return r.read().decode()

def main():
    light_sensor = GroveLightSensor(LIGHT_PIN)   # Cảm biến ánh sáng
    distance_sensor = GroveUltrasonicRanger(ULTRASONIC_PIN)   # Cảm biến khoảng cách (cm)
    lcd = JHD1802()   #LCD

    led = LED(LED_PIN)   # LED bật/tắt
    buzzer = GroveBuzzer(BUZZER_PIN)   # Buzzer bật/tắt

    # Output: Gửi dữ liệu lên thingspeak
    # Output: Terminal và LCD

    print_counter = 0
    write_counter = 0

    try:
        while True:
            value1 = light_sensor.value
            value2 = distance_sensor.get_distance()

            #In ra LCD và màn hình mỗi 10s
            if (print_counter >= 10):
                print_counter = 0
                print(f"Light Value: {value1}, Distance Value: {value2}")
                lcd.setCursor(0,0)
                lcd.write(f"Light: {value1:3}")
                lcd.setCursor(1,0)
                lcd.write(f"Distance: {value2:2} cm")
            else:
                print_counter += 1

            #LED
            if (value1 > 500):
                led.on()
            elif (value1 < 300):
                led.off()

            #BUZZER
            if (value2 < 30):
                buzzer.on()
            elif (value2 > 60):
                buzzer.off()


            # Data lên server
            if (write_counter >= 20):
                write_counter = 0
                thingspeak_write({1: value1, 2: value2 })
            else:
                write_counter += 1
            sleep(1)
    except KeyboardInterrupt:
        print("Đã dừng chương trình!")
    finally:
        led.off()
        buzzer.off()


if __name__ == "__main__":
    main()