import time
import board
import pwmio
 
led = pwmio.PWMOut(board.D26, frequency=75000, duty_cycle=00000) #65535 is max, 32767 is 50%