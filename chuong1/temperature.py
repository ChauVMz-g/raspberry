#CẢM BIẾN NHIỆT ĐỘ

import Adafruit_DHT

sensor = Adafruit_DHT.DHT22
SENSOR_PIN = 16
print("Please wait...!!!")

humidity, temperature = Adafruit_DHT.read_retry(sensor, SENSOR_PIN)

if humidity is not None and temperature is not None:
    print('Temp: {0:0.1f}*C Humidity = {1:0.1f}%'.format(temperature, humidity))
else:
    print('Failed to get reading. Try again!')