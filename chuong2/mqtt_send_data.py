import paho.mqtt.client as mqtt
from time import sleep
from random import randint

channelId = 3568107
username = 'GwsKIxkcJjwLJDQZIzo0HhI'
clientId = 'GwsKIxkcJjwLJDQZIzo0HhI'
password = 'voRTtpGdrWyCAwVvFAj6W64W'

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, clientId)
client.username_pw_set(username=username, password=password)
client.connect("mqtt3.thingspeak.com", 1883, 60)

def thingspeak_mqtt(data1, data2):
    client.publish("channels/%s/publish" %(channelId), "field1=%s&field2=%s&status=MQTTPUBLISH" %(data1, data2))

while True:
    data_random1 = randint(0,50)
    data_random2 = randint(0,100)
    print("Nhiet do: " , data_random1, " Do am: ", data_random2)

    thingspeak_mqtt(data_random1, data_random2)
    sleep(20)