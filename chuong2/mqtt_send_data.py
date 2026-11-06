import paho.mqtt.client as mqtt
from time import sleep
from random import randint

channelId = 3568107
username = 'PAYoOyQgKgIEGgAHDy8cGgw'
clientId = 'PAYoOyQgKgIEGgAHDy8cGgw'
password = 'eD7A/jynesN0/F1yDfR/EEwI'

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, clientId)
client.username_pw_set(username=username, password=password)
client.connect("mqtt3.thingspeak.com", 1883, 60)

def thingspeak_mqtt(data):
    client.publish("channels/%s/publish" %(channelId), "field3=%s&status=MQTTPUBLISH" %(data))

while True:
    data_random = randint(0,50)
    print (data_random)

    thingspeak_mqtt(data_random)
    sleep(20)