import sys
from time import sleep
import paho.mqtt.client as mqtt
from random import randint

CHANNEL_ID = "3570604"
CLIENT_ID = "EjA0IRokGyITOiseHgAIHws"
USERNAME = "EjA0IRokGyITOiseHgAIHws"
PASSWORD = "F9tj4Lk8MEh4zPBANnf+Hypu"
BROKER_HOST = "mqtt3.thingspeak.com"
PUBLISH_INTERVAL = 20

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, CLIENT_ID)
client.username_pw_set(username=USERNAME, password=PASSWORD)
client.connect(BROKER_HOST, 1883, 60)
client.loop_start()

def publish(field1, field2):
  topic = f"channels/{CHANNEL_ID}/publish"
  payload = f"field1={field1}&field2={field2}&status=OK"
  client.publish(topic, payload)

def main():
    try:
        while True:
            temp = randint(0, 50)
            humid = randint(50, 100)
            publish(field1=temp, field2=humid)
            print(f"Temperature: {temp}C, Humidity: {humid}")
            sleep(20)
    except KeyboardInterrupt:
        print("Đã dừng chương trình")
    finally:
        client.loop_stop()
        client.disconnect()

if __name__ == "__main__":
    main()