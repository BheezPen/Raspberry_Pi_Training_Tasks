from machine import Pin
from time import sleep

ledYellow = Pin(15, Pin.OUT)
ledBlue = Pin(11, Pin.OUT)
ledBlack = Pin(7, Pin.OUT)

while True:
    ledYellow.on()
    ledBlue.on()
    sleep(0.1)
    ledYellow.off()
    sleep(0.01)
    #ledBlue.on()
    #sleep(0.1)
    #ledBlue.off()
    #sleep(0.01)
    ledBlack.on()
    sleep(0.1)
    ledBlack.off()
    sleep(0.01)