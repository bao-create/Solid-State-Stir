from os import name
import time
import multiprocessing
from simple_pid import PID
from gui_code import gui_run
import statistics as stat
from temp_function import *


def pid_proc(system_state, data_state):
    pid = PID(3000,0,0) #init PID object with P, I and D parameters
    pid.sample_time = .1 #how often the pid creates an output
    pid.output_limits =(0,65535)
    
    pwm_object = gpio_pwm(0) #holding this object so that the output stays on
    
    num_thermos = 1
    max_var = temp_init(num_thermos) #init thermocople spi interface
    
    
    

    while not system_state.exit: #also long as we havent gotten controller kill from gui
        if system_state.run:
            pid.setpoint = system_state.setpoint
            for i in range(0,num_thermos): #read all the thermos
                data_state.temp[i] = max_var[i].temperature
            
            data_state.time = time.time()

            if control_state.controllocation: #if we are reading data from bed or substrate
                output = pid(stat.mean(data_state.temp[6:11]))
            else:
                output = pid(stat.mean(data_state.temp[0:1])) #modified for testing
        else:
            output = 0
    
        data_state.power = output
        pwm_object.duty_cycle=output
        time.sleep(.1)
    

    return





if __name__ == '__main__':
    with multiprocessing.Manager() as manager:
        
        system_state = manager.Namespace() #creates a simple class that has no methods only written by gui process
        system_state.pid_run = False
        system_state.sub_thermo_exist = False
        system_state.control_location = False # PID from the bed(false) or substrate (true)
        system_state.setpoint = 400
        system_state.exit = False


        data_state = manager.Namespace() #only written by pid process
        data_state.temp = [0,0,0,0,0,0,0,0,0,0,0,0]
        data_state.power = []
        data_state.time = []

    p1 = multiprocessing.Process(target=gui_start, args=(system_state, data_state))
    p2 = multiprocessing.Process(target=pid_proc, args=(system_state, data_state)) 

    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('Clean Exit')
