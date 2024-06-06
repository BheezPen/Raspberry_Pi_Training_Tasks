from machine import Pin
from time import sleep

ledRed = Pin(15, Pin.OUT)

while True:
    ledRed.on()
    sleep(0.1)
    ledRed.off()
    sleep(0.01)
    