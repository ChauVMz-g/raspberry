#LED

from gpiozero import LED
from time import sleep

LED_PIN = 17

led = LED(LED_PIN)

try:
    while(True):
        led.on()
        sleep(1)
        led.off()
        sleep(1)
except KeyboardInterrupt:
    led.off()
    print("Đã dừng chương trình và tắt LED.")
