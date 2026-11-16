"""
import sys, time, math
from grove.adc import ADC

LIGHT_PIN = 0   #Channel A0

class GroveLightSensor:
    def __init__(self, channel):
        self.channel = channel
        self.adc = ADC()

    @property
    def light(self):
        value = self.adc.read(self.channel)
        return value

sensor = GroveLightSensor(LIGHT_PIN)

print("Detecting light....")
while True:
    print(f'Light value: {sensor.light}')
    time.sleep(1)
"""


import time
import sys
from grove.grove_light_sensor_v1_2 import GroveLightSensor

# Cắm vào cổng A0 trên Grove Base Hat
sensor = GroveLightSensor(0)

print("Đang đọc giá trị ánh sáng từ thư viện grove.py...")

try:
    while True:
        # Thuộc tính .light đã được viết sẵn trong thư viện
        light_value = sensor.light
        print(f"Giá trị ánh sáng: {light_value}")
        time.sleep(1)

except KeyboardInterrupt:
    print("\nĐã dừng chương trình.")
    sys.exit(0)