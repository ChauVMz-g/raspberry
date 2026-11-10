import sys
from time import sleep

import paho.mqtt.client as mqtt


SENSOR_PIN = 5
LED_PIN = 6
SERVO_PIN = 18
BUZZER_PIN = 12


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


  def main():
    pass


if __name__ == "__main__":
   main()