import ahtx0
from machine import Pin, I2C
from time import sleep

i2c = I2C(1, scl=Pin(15), sda=Pin(14))

sensor = ahtx0.AHT10(i2c)


while True:
    print("Temperature: ",sensor.temperature)
    sleep(0.5)
    print("Humidity: ", sensor.relative_humidity)
    sleep(0.5)
    if sensor.temperature >= 28:
        print("Temperature Is Greater Than 28\n")
        
        
    