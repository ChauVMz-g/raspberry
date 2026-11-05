from urllib import request, parse
from time import sleep
from random import randint

# Channel ID: 
# Author: 
# API Key (Write):  
# API Key (Read): 

def make_param_thingspeak(data):
    params = parse.urlencode({'field1': data}).encode()
    return params

def thingspeak_post(params):
    api_key_write = ""
    req = request.Request('https://api.thingspeak.com/update', method="POST")
    req.add_header("Content-Type", "application/x-www-form-urlencoded")
    req.add_header("X-THINGSPEAKAPIKEY", api_key_write)
    r = request.urlopen(req, data = params)
    respone_data = r.read()
    return respone_data

while True:
    data_random = randint(0,50)
    print(data_random)

    params_thingspeak = make_param_thingspeak(data_random)
    thingspeak_post(params_thingspeak)

    sleep(20)