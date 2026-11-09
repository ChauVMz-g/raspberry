"""
from gpiozero import Buzzer
from signal import pause

BUZZER_PIN = 12

buzzer = Buzzer(BUZZER_PIN)
buzzer.beep(0.1, 1) # ON = 0.1s, OFF = 1s

pause()

"""

from grove.gpio import GPIO
import sys, time

BUZZER_PIN = 12

class GroveBuzzer(GPIO):
    def __init__(self, pin):
        super(GroveBuzzer, self).__init__(pin, GPIO.OUT)

    def on(self):
        self.write(1)

    def off(self):
        self.write(0)

buzzer = GroveBuzzer(BUZZER_PIN)

while True:
    try:
        buzzer.on()
        time.sleep(0.1)
        buzzer.off()
        time.sleep(1)
    except KeyboardInterrupt:
        buzzer.off()
        print('exit')
        exit(1)

"""

import time
import sys
from grove.grove_buzzer import GroveBuzzer

buzzer = GroveBuzzer(12)

try:
    while True:
        buzzer.on()
        time.sleep(0.1)
        buzzer.off()
        time.sleep(1.0)
except KeyboardInterrupt:
    buzzer.off()
    sys.exit(0)

"""