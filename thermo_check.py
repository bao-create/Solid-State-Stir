import time
import board
import busio
import digitalio
import adafruit_max31855
import pwmio

import time
import csv

def get_temp():
    spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
    cs_pin_list = [board.D5,board.D6]
    output = [1,1]
    
    for i in range(0,2):
        
        cs_var = digitalio.DigitalInOut(cs_pin_list[i])
        max_var = adafruit_max31855.MAX31855(spi,cs_var)
        output[i] = max_var.temperature
        
    return output    
    
def gpio_pwm(output):
    
    pwm = pwmio.PWMOut(board.D26, frequency = 10000, duty_cycle=output) 
    
    pwm.direction = digitalio.Direction.OUTPUT
    time.sleep(.5)
    print("in gpio_pwm funct")
    return
data = []
while True:
    x = get_temp()
    
    
    
    print(x)
        
        
    time.sleep(.5)