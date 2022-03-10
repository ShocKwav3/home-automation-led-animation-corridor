from machine import Pin
from time import sleep


builtInLed = Pin(2, Pin.OUT)

while True:
    builtInLed.value(1)
    sleep(2)
    builtInLed.value(0)
    sleep(2)