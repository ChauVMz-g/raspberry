from urllib import request, parse
from time import sleep
import json

#Channel ID: 3568107
#Author: mwa0000037711030
#API Key (Write): 5HOOHU5I7V50O07H
#API Key (Read): 491MYM357SKR19ES

def thingspeak_get():
    api_key_read = "491MYM357SKR19ES"
    channel_ID = "3568107"
    req = request.Request("https://api.thingspeak.com/channels/%s/fields/1/last.json?api_key=%s" % (channel_ID, api_key_read), method="GET")
    r = request.urlopen(req)
    respone_data = r.read().decode()
    respone_data = json.loads(respone_data)
    value = respone_data['field1']
    return value

value = thingspeak_get()
print(value)