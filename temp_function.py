import time
import board
import busio
import digitalio
import adafruit_max31855
import pwmio


def output = get_temp():
    spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
    cs_pin_list = [4,5,6,12,13,16,17,18,19,20,21,22,23]
    output = [0,0,0,0,0,0,0,0,0,0]
    for i in range(0,9):
        cs_string = "board"+"D"+str(cs_pin_list(i))
        cs_var = digitalio.DigitalInOut(cs_string)
        max_var = adafruit_max31855.MAX31855(spi,cs_var)
        output(i) = max_var.temperature
        
    
def gpio_pwm(output);
    
    pwm = pwmio.PWMOut(board.D24, frequency = 10000, duty_cycle=output)
    
    pwm.direction = digitalio.Direction.OUTPUT
    