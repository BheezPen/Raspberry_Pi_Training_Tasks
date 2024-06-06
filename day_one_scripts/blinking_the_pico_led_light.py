from machine import Pin
from time import sleep
led = Pin("LED",Pin.OUT) # This instantiate the Class (i.e create object) to put on the LED on the microcontroller
led.value(0) # Give argument 1 to put on and 0 to put off
'''
while True: #THis loop the blink the led light
    led.on()
    sleep(1)
    led.off()
    sleep(1)
'''

while True: # So this does same, the toggle function does the work of blinking Led.
    led.toggle() # Switch the state of the toggle
    sleep(1) 