import time
import board
import busio
import digitalio
import adafruit_max31855
import pwmio

import time

def get_temp(power_output,pwm_object,max_var,counter):
    spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
    cs_pin_list = [board.D4,board.D5,board.D6,board.D12,board.D13,board.D16,board.D17,board.D18,board.D19,board.D20,board.D21,board.D22,board.D23]
    output = [0,0,0,0,0,0,0,0,0,0]
    #pwm_object.duty_cycle = 0
    pwm_object.duty_cycle=power_output
    if counter == 0:
        max_var = []
        for i in range(0,1):
            
            cs_var = digitalio.DigitalInOut(cs_pin_list[i])
            max_var_single = adafruit_max31855.MAX31855(spi,cs_var)
            max_var = max_var + [max_var_single]
            output[i] = max_var_single.temperature
    else:
        #print(max_var)
        for i in range(0,1):
            output[i] = max_var[i].temperature
    print("gpio power output:",power_output)
    #pwm_object.duty_cycle=power_output
    #x=gpio_pwm(power_output)
    time.sleep(.1)
    
    return output,pwm_object,max_var    
    
def gpio_pwm(output):
    
    pwm = pwmio.PWMOut(board.D26, frequency = 100000, duty_cycle=output)
    
    #pwm.direction = digitalio.Direction.OUTPUT
    #time.sleep(.5)
    #print("in gpio_pwm funct")
    #x = input("press any")
    return pwm

#x = gpio_pwm(65535)
#d= get_temp(65535,x)
