from gpiozero import LED
from signal import pause

led = LED(5)
led.blink(0.3, 1, 5)

pause()