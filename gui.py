import threading
from queue import Queue
import time
import simple-PID
from tkinter_py_code.py import gui_start
#from pid_shit.py import pid_init
from temp_function.py import *
import statistics as stat

class Thread_maker (threading.Thread): #makes the threads with names
   def __init__(self, threadID, name,target_line,args_line):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.target = target_line
      self.args=args_line

      return
class system_state: # system state class, needs to be updated with rosses code
  def __init__ (self, run, temp, subthermoexist, controllocation, setpoint,time_pid,power):
    self.run = False #are we running the system
    self.temp = [0,0,0,0,0,0,0,0,0,0,0,0,0] #temperature array, thermos 1-13
    self.subthermoexist = False #
    self.controlloation = True #PID from the bed(false) or substrate (true)
    self.setpoint = 400    #temp setpoint
    self.time_pid = time.time()
    self.power = 0
    return


def pid_init(q): # this is going to be either the main.py file or its own.
  
  pid = PID(1,1,1) #init PID object with P, I and D parameters
  pid.sample_time = .1 #how often the pid creates an output
  while True: #pid loop
    state = q.get() #get the current data for run and setpoint
    if state.run:
      pid.setpoint = state.setpoint() #set the setpoint based on GUI
      
      current_temp = get_temp()
      #do the serial read shit based on number of thermocouples, and 


      #current_temp = [1,1,1,1,1,1,1,1,1,1,1,1,1] #full array of TC values
      state.temp = current_temp #update state variable
      state.time_pid = time.time() #update time when this was taken
      if state.controllocation: #if we are pulling data from top plate or substrate
          
          output = pid(stat.mean(state.temp[6:1])) #get the PID output where 1:4 is a placeholder for the state varible controlling what TC are controlling the temp
      else:
          output = pid(stat.mean(state.temp[0:3]))
    else: #if run=false
      output = 0 #no input to SCR
      
    #do gpio pwm shit to the low pass filter to control the power
    state.power = output #return what the SCR should be getting
    gpio_pwm(output)

    q.put(state) #update temperature and state variables
    q.task_done() #not sure what .task_done is. part of queue lib.

    time.sleep(pid.sample_time) # slow down the PID loop



q = Queue() #the queue object for passing info back and forth

gui_thread = Thread_maker(1, "gui_thread",gui_start,(q, )) #thread creation for gui and pid idk if this is right
pid_thread = Thread_maker(2, "pid_thread",pid_init,(q, ))
  
#might need .start() calls here
