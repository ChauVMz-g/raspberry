import paho.mqtt.client as mqtt
from time import sleep
from random import randint

# Channel ID: 794872
# username = JiQ0BAc1DSU5EzgtJishCBQ
# clientId = JiQ0BAc1DSU5EzgtJishCBQ
# password = cVQTrLjDdgwSCFMpETyQERX3

client = mqtt.Client("JiQ0BAc1DSU5EzgtJishCBQ")
client.username_pw_set(username="JiQ0BAc1DSU5EzgtJishCBQ", password="cVQTrLjDdgwSCFMpETyQERX3")
client.connect("mqtt3.thingspeak.com", 1883, 60)

def thingspeak_mqtt(data):
    channel_ID = "794872"
    client.publish("channels/%s/publish" %(channel_ID), "field3=%s&status=MQTTPUBLISH" %(data))

while True:
    data_random = randint(0,50)
    print (data_random)

    thingspeak_mqtt(data_random)
    sleep(20)