import sys
import time

import RPi.GPIO as IO
from numpy import interp
SERVO_PIN = 12
IO.setwarnings(False)
IO.setmode(IO.BCM)

class GroveServo:
    MIN_DEGREE = 0
    MAX_DEGREE = 180
    INIT_DUTY = 2.5

    def __init__(self, channel):
        IO.setup(channel, IO.OUT)
        self.pwm = IO.PWM(channel, 50)
        self.pwm.start(GroveServo.INIT_DUTY)

    def __del__(self):
        self.pwm.stop()

    def setAngle(self, angle):
        angle = max(min(angle, GroveServo.MAX_DEGREE), GroveServo.MIN_DEGREE)
        tmp = interp(angle, [0, 180], [25, 125])
        self.pwm.ChangeDutyCycle(round(tmp/10.0, 1))

servo = GroveServo(SERVO_PIN)

while(True):
    for x in range(0, 180, 10):
        print(x, "degree")
        servo.setAngle(x)
        time.sleep(0.1)

    for x in range(180, 0, -10):
        print(x, "degree")
        servo.setAngle(x)
        time.sleep(0.1)