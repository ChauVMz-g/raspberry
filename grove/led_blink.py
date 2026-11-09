from gpiozero import LED
from signal import pause

LED_PIN = 5

led = LED(LED_PIN)
led.blink(0.3, 1, 5)

pause()

