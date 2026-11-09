#NÚT NHẤN

from gpiozero import Button
from time import sleep

BUTTON_PIN = 2

button = Button(BUTTON_PIN)

try:
    while(True):
        if button.is_pressed:
            print("Button is pressed")
        else:
            print("Button is not pressed")
        sleep(0.1)
except KeyboardInterrupt:
    print("Đã dừng chương trình")