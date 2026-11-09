#CẢM BIẾN KHOẢNG CÁCH

from gpiozero import DistanceSensor
from time import sleep

ECHO_PIN = 23
TRIGGER_PIN = 24

sensor = DistanceSensor(echo=ECHO_PIN, trigger=TRIGGER_PIN)
while True:
    print("Distance to nearest object is", sensor.distance, 'm')
    sleep(1)