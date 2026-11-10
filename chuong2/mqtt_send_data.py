import paho.mqtt.client as mqtt
from time import sleep
from random import randint

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

while True:
    data_random1 = randint(0,50)
    data_random2 = randint(0,100)
    print("Nhiet do: " , data_random1, " Do am: ", data_random2)

    publish(data_random1, data_random2)
    sleep(20)