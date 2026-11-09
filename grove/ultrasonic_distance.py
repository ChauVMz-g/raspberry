import time
from grove.grove_relay import GroveRelay
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger

ULTRASONIC_PIN = 5
RELAY_PIN = 16

#Grove - Ultrasonic Ranger connected to port D5
sensor = GroveUltrasonicRanger(ULTRASONIC_PIN)

#Grove - Relay connected to port D16
relay = GroveRelay(RELAY_PIN)

while True:
    distance = sensor.get_distance()
    print('Distance: {} cm'.format(distance))

    if distance < 20:
        relay.on()
        print('relay on')

    else:
        relay.off()
        print('relay off')

    time.sleep(1)