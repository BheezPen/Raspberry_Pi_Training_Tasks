"""This project help Apple Farmers monitor the Temperature on the farm. It also detect Motions and monitors how close the motions is. 
This helps watchout for birds coming close to the plants. 
When the system is on, and everything looks good, the GREEN light comes On.
When the temperatues is low or higher, (i set the threshold between 20 celcuis to 25 Celcius for a normal system), the Yellow Light Blinks 
When Motion is Detected, the Red Light Blinks
When Detected motion is 20cm closer, the Red Light is On.
"""
from machine import Pin
from time import sleep

import ahtx0
from machine import Pin, I2C
from time import sleep



from hcsr04 import HCSR04

#sensor = HCSR04(trigger_pin=15, echo_pin = 14)
'''
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
    
'''
# The Led Light
LedGreenNormal = Pin(2, Pin.OUT)
LedYellowLowTemp = Pin(6, Pin.OUT)
LedRedBlinks = Pin(17, Pin.OUT)
LedRedStagnant = Pin(21, Pin.OUT)

'''
while True:
    LedGreenNormal.on()
    LedYellowLowTemp.on()
    LedRedBlinks.on()
    LedRedStagnant.on()
    sleep(2)
    
    LedGreenNormal.off()
    LedYellowLowTemp.off()
    LedRedBlinks.off()
    LedRedStagnant.off()
    sleep(2)
'''

# The Sensor
SoundSensor = HCSR04(trigger_pin=15, echo_pin = 14)


i2c = I2C(1, scl=Pin(11), sda=Pin(10))
#TempSensor = ahtx0.AHT10(i2c)

pir = Pin(15,Pin.IN, Pin.PULL_DOWN)

MotionSensor = Pin(3,Pin.IN, Pin.PULL_DOWN)
sleep(1)

print('Ready')

sensor_temperature = 20
pir_value = 1
#distance = 3	
distance = SoundSensor.distance_cm()
print('distance is', distance)
while True:
    if 20 <= sensor_temperature <= 25: # 20 <= TempSensor.temperature <= 25: #20 <= sensor.temperature <= 25:	# 
        print('Temperature is fine')
        if MotionSensor.value() == 0: #pir.value():
            print("Motion Not Detected")
            sleep(1)
            print("Green")
            LedGreenNormal.on()
            #print("Distance is ", distance, "cm")
        elif MotionSensor.value() == 1:
            print("Motion Detected")
            print("Red Blinks")
            if distance >= 20:
                LedRedBlinks.on()
                sleep(0.2)
                LedRedBlinks.off()
                sleep(0.2)
                print("Motion distance is ", distance, "cm")
                
            if distance <= 20:
                print("Motion distance is ", distance, "cm and very close")
                print("Red is Stagnant")
                LedRedStagnant.on()
                #ledRed.off()
                #sleep(0.5)
    else:
        print("Temperature is Higher or Higher")
        print("Yellow Blinks")
        LedYellowLowTemp.on()
        sleep(0.2)
        LedYellowLowTemp.off()
        sleep(0.2)
    #sleep(10)
    
    
    LedGreenNormal.off()
    LedYellowLowTemp.off()
    LedRedBlinks.off()
    LedRedStagnant.off()
    sleep(1)
            
"""
print("Temperature: ",sensor.temperature)
    sleep(0.5)
    print("Humidity: ", sensor.relative_humidity)
    sleep(0.5)
    if sensor.temperature >= 28:
        print("Temperature Is Greater Than 28\n")
        
"""        