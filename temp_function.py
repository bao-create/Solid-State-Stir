import time
import board
import busio
import digitalio
import adafruit_max31855
import pwmio

import time

def get_temp(output):
    spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
    cs_pin_list = [board.D4,board.D5,board.D6,board.D12,board.D13,board.D16,board.D17,board.D18,board.D19,board.D20,board.D21,board.D22,board.D23]
    output = [0,0,0,0,0,0,0,0,0,0]
    gpio_pwm(0)
    for i in range(0,9):
        
        cs_var = digitalio.DigitalInOut(cs_pin_list[i])
        max_var = adafruit_max31855.MAX31855(spi,cs_var)
        output[i] = max_var.temperature
    gpio_pwm(output)
    return output    
    
def gpio_pwm(output):
    
    pwm = pwmio.PWMOut(board.D26, frequency = 10000, duty_cycle=output)
    
    pwm.direction = digitalio.Direction.OUTPUT
    time.sleep(.5)
    print("in gpio_pwm funct")
    return
x=get_temp()
print(x)
