import time
import board
import pwmio
 
led = pwmio.PWMOut(board.D26, frequency=100000, duty_cycle=0) #65535 is max, 32767 is 50%