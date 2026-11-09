#NÚT NHẤN + LED

from gpiozero import LED, Button
from signal import pause

LED_PIN = 17
BUTTON_PIN = 2

led = LED(LED_PIN)
button = Button(BUTTON_PIN)

button.when_pressed = led.on
button.when_released = led.off

#Cách 2:
#button.when_pressed = led.toggle

pause()