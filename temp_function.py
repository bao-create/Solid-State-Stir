import time
import board
import busio
import digitalio
import adafruit_max31855
import pwmio

import time

def get_temp():
    spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
    cs_pin_list = [board.D4,board.D5,board.D6,board.D12,board.D13,board.D16,board.D17,board.D18,board.D19,board.D20,board.D21,board.D22,board.D23]
    output = [0,0,0,0,0,0,0,0,0,0]
    
    for i in range(0,9):
        
        cs_var = digitalio.DigitalInOut(cs_pin_list[i])
        max_var = adafruit_max31855.MAX31855(spi,cs_var)
        output[i] = max_var.temperature
    return output    
    
def gpio_pwm(output):
    
    pwm = pwmio.PWMOut(board.D17, frequency = 10000, duty_cycle=output)
    
    pwm.direction = digitalio.Direction.OUTPUT
    time.sleep(1)
    print("in gpio_pwm funct")
    return
x=gpio_pwm(1)
print(x)