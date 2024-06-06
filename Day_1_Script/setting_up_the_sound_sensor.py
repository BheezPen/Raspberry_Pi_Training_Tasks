from hcsr04 import HCSR04

from time import sleep

from machine import Pin

sensor = HCSR04(trigger_pin=15, echo_pin = 14)

ledRed = Pin(13, Pin.OUT)
while True:
    distance = sensor.distance_cm()
    print("Distance is ", distance, "cm")
    if distance <= 20:
        ledRed.on()
        sleep(0.5)
        ledRed.off()
        sleep(0.5)
    else:
        ledRed.off()
        sleep(0.5)
    
