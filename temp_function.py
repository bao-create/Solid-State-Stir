import time
import board
import busio
import digitalio
import adafruit_max31855
import pwmio

def temp_init(num_thermos):
    cs_pin_list = [board.D4,board.D5,board.D6,board.D12,board.D13,board.D16,board.D17,board.D18,board.D19,board.D20,board.D21,board.D22,board.D23]
    max_var = []
    spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
    # only look at first thermocouple (#0)
        for i in range(0,num_thermos):
            cs_var = digitalio.DigitalInOut(cs_pin_list[i])
            max_var_single = adafruit_max31855.MAX31855(spi,cs_var)
            max_var = max_var + [max_var_single]
    return max_var

# def get_temp(power_output,pwm_object,max_var,init,spi):
    
#     cs_pin_list = [board.D4,board.D5,board.D6,board.D12,board.D13,board.D16,board.D17,board.D18,board.D19,board.D20,board.D21,board.D22,board.D23]
#     output = [0,0,0,0,0,0,0,0,0,0]    
#     pwm_object.duty_cycle=power_output
#     if init:
#         max_var = []
#         # only look at first thermocouple (#0)
#         for i in range(0,1):
#             spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
#             cs_var = digitalio.DigitalInOut(cs_pin_list[i])
#             max_var_single = adafruit_max31855.MAX31855(spi,cs_var)
#             max_var = max_var + [max_var_single]
#             output[i] = max_var_single.temperature
#     else:
#         #print(max_var)
#         for i in range(0,1):
#             output[i] = max_var[i].temperature
#     print("gpio power output:",power_output)    
#     time.sleep(.1)    
#     return output,pwm_object,max_var,spi    
    
def gpio_pwm(output):       
    pwm = pwmio.PWMOut(board.D26, frequency = 100000, duty_cycle=output)       
    return pwm