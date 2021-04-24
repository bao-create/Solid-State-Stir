from os import name
import threading
from queue import *
import time
from simple_pid import PID
from gui_code import gui_start
#from pid_shit.py import pid_init
#from temp_function.py import *
import statistics as stat
from temp_function import *

class Thread_maker (threading.Thread): #makes the threads with names
   def __init__(self, threadID, name,target_line,args_line):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.target = target_line
      self.args=args_line

      return
class system_state: # system state class, needs to be updated with rosses code
  def __init__ (self):
      self.run = False #are we running the system
      #self.temp = [0,0,0,0,0,0,0,0,0,0,0,0,0] #temperature array, thermos 1-13
      self.subthermoexist = False #
      self.controllocation = True #PID from the bed(false) or substrate (true)
      self.setpoint = 400    #temp setpoint
      #self.time_pid = time.time()
      #self.power = 0
      return

class data_state_class:
  def __init__ (self):
    self.temp=[0,0,0,0,0,0,0,0,0,0,0,0]
    self.power=[]
    self.time = []
    return


def pid_init(q,data_q): # this is going to be either the main.py file or its own.
  
  pid = PID(3000,0,0) #init PID object with P, I and D parameters
  pid.sample_time = .1 #how often the pid creates an output
  pid.output_limits =(0,65535)
  data_state = data_state_class()
  
  while True: #pid loop
    
     
    if not q.empty():
      control_state = q.get(block=True,timeout=1) #get the current data for run and setpoint
      
    
        
        
    
    
    #print("in pid while before data_state run",data_state.temp)
    
    if control_state.run:
      pid.setpoint = control_state.setpoint #set the setpoint based on GUI
      
      current_temp = get_temp()
      #do the serial read shit based on number of thermocouples, and 
      

      #current_temp = [1,1,1,1,1,1,1,1,1,1,1,1,1] #full array of TC values
      data_state.temp = current_temp #update data_state variable
      data_state.time = time.time() #update time when this was taken
      if control_state.controllocation: #if we are pulling data from top plate or substrate
          
          output = pid(stat.mean(data_state.temp[6:11])) #get the PID output where 1:4 is a placeholder for the data_state varible controlling what TC are controlling the temp
      else:
          output = pid(stat.mean(data_state.temp[0:3]))
    else: #if run=false
      output = 0 #no input to SCR
      
    #do gpio pwm shit to the low pass filter to control the power
    data_state.power = output #return what the SCR should be getting
    print(output)
    gpio_pwm(output)
#     print("temp",data_state.temp)
    
    
    data_q.put(data_state) #update temperature and data_state variables
    #q.taskdone() #not sure what .task_done is. part of queue lib.

    time.sleep(pid.sample_time) # slow down the PID loop
    
    


init_data_q_state = data_state_class()
init_control_q = system_state()
q = LifoQueue() #the queue object for passing info back and forth
data_q = LifoQueue()
data_q.put(init_data_q_state)
q.put(init_control_q)
gui_thread = threading.Thread(name="gui_thread",target=gui_start,args=(q,data_q )) #thread creation for gui and pid idk if this is right
pid_thread = threading.Thread(name="pid_thread",target=pid_init,args=(q,data_q ))


gui_thread.start()
print("Before 2 start")
pid_thread.start() 


print("after start") 
gui_thread.join()
print("after gui join")
pid_thread.join()
print("after pid join")

#might need .start() calls here