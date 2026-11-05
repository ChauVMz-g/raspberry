from urllib import request, parse
from time import sleep
import json

#Channel ID:
#Author:
#API Key (Write): 
#API Key (Read):

def thingspeak_get():
    api_key_read = "API_KEY_READ"
    channel_ID = "CHANNEL_ID"
    req = request.Request("https://api.thingspeak.com/channels/%s/fields/1/last.json?api_key=%s" % (channel_ID, api_key_read), method="GET")
    r = request.urlopen(req)
    respone_data = r.read().decode()
    respone_data = json.loads(respone_data)
    value = respone_data['field1']
    return value

value = thingspeak_get()
print(value)