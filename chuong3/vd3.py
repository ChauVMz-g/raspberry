from gpiozero import LED
from urllib import request, parse
from time import sleep
import json

# Channel ID: 794872
# Author: iotlabiuh
# API Key (Write): VN9L7BBX6YI4LWJ3
# API Key (Read): VSOKXS2QDTNC3Z30

red = LED(5)

def thingspeak_get():
    api_key_read = "VSOKXS2QDTNC3Z30"
    channel_ID = "794872"
    req = request.Request("https://api.thingspeak.com/channels/%s/fields/1/last.json?api_key=%s" % (channel_ID, api_key_read), method="GET")
    r = request.urlopen(req)
    respone_data = r.read().decode()
    respone_data = json.loads(respone_data)
    value = respone_data['field1']
    return value

while True:
    value = thingspeak_get()
    print(value)

    if (value == "1"):
        red.on()
    else:
        red.off()