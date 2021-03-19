#Imports
from tkinter import *
from tkinter import font
import tkinter as tk
from tkinter import ttk
#import matplotlib.pyplot as plt
#import matplotlib
import matplotlib.animation as animation
from matplotlib import style
import csv
from queue import Queue
style.use('ggplot')

#Defining Class
class system_state:
  def init (self, run, temp, subthermoexist, controllocation, setpoint,time_pid,power):
    self.run = False #are we running the system
    self.temp = [0,0,0,0,0,0,0,0,0,0,0,0,0] #temperature array, thermos 1-13
    self.subthermoexist= False #Does the Substrate thermocouple exist
    self.controllocation = True #PID from the bed(false) or substrate (true)
    self.setpoint = 400    #temp setpoint in c
    self.time_pid = time.time()
    self.power = 0
    return


def graph():
    temp_stored=temp_stored.append+Currentstate.temp
    Time_pid_stored=Time_pid_stored.append+Currentstate.time_pid
    ax.plot(xdata1, ydata1, color='tab:blue')
    ax.plot(xdata2, ydata2, color='tab:orange')
    plt.ylabel('Temperature, C')
    plt.xlabel('Time, s')
    plt.show()
    counter=counter+1
def set_state():
    Currentstate.subthermoexist = isSubstrate_Thermocouple_Value.get()
    Currentstate.controllocation = isPID_Option_Value.get()
    Currentstate.setpoint = Temp_Set.get()
    Currentstate.run = isRunning.get()
    print(Currentstate.run)
    print(Currentstate.setpoint)
    print(Currentstate.controllocation)
    print(Currentstate.subthermoexist)
    #insert threading communication code here!!!!
    q.put(Currentstate)
    
    get_state()
    
#Functions for on and off buttons; updates retrieve
def data_save():
    with open(Save_name.get(), 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     wr.writerows(data_log_array)
def data_on():
    log_data = True
    return
def data_off():
    log_data = False
    return

def on():
    isRunning.set(True)
    set_state()
    return
def off():
    isRunning.set(False)
    set_state()
    return
def get_state():
    # do the queue operations
    Currentstate = q.get()
    if log_data:
        data_log_array.append(Currentstate.temp)
    return
def gui_start(queue_obj):
    #Now we get into tkinter
    #Defines overall box
    global q,Currentstate,log_data,data_log_array, isRunning,Temp_Set, isPID_Option_Value,isSubstrate_Thermocouple_Value,Save_name #global variables becasue button commands cannot pass arguments and we need the q object passed
    q = queue_obj #get quene object local to this file
    #Defines an object of class system_state
    Currentstate=system_state()
    log_data = False
    data_log_array = []
    #==================== Back End
    Time_pid_stored=0
    temp_stored=[0,0,0,0,0,0,0,0,0,0,0,0,0]
    #Retrieve updates currentstate object
    root = Tk()
    root.geometry("1000x1000")
    root.title("AFSD Print Bed Interface")

    #Font, Text, and scaling, graphs
    ftitle = font.Font (family="Helvetica",size=30,weight="bold")
    fbody  = font.Font (family="Helvetica",size=12)
    #style.use("ggplot")

    #==================== Front End

    #Top Label
    Title_Label = Label(root, text = "AFSD Heated Print Bed Interface", font = ftitle)
    Title_Label.place(x = 10, y = 0)

    #Temperature Set Point
    Temp_Label = Label(root, text = "Enter your target temperature in Celcius:", font = fbody)
    Temp_Label.place(x = 10, y = 50)
    Temp_Set = Entry(root, bd = 3)
    Temp_Set.place(x = 300, y = 50)
    Temp_Set.insert(0,'###')

    #Enabling Substrate Thermocouples
    isSubstrate_Thermocouple_Value = BooleanVar()

    Substrate_Thermocouple_Label = Label(root, text = "Are there Thermocouples on your substrate?", font = fbody)
    Substrate_Thermocouple_Label.place(x = 10, y = 100)

    Substrate_Thermocouple_Yes = Radiobutton(root, text = "Yes", variable = isSubstrate_Thermocouple_Value, value = True)
    Substrate_Thermocouple_Yes.place(x = 10, y = 150)
    
    Substrate_Thermocouple_No = Radiobutton(root, text = "No", variable = isSubstrate_Thermocouple_Value, value = False)
    Substrate_Thermocouple_No.place(x = 10, y = 200)

    #PID Control Selection Menu
    isPID_Option_Value = BooleanVar()

    PID_Control_Label = Label(root, text = "Which part should the temperature PID control-loop be based on?", font = fbody)
    PID_Control_Label.place(x = 410, y = 100)

    PID_Option_Substrate = Radiobutton(root, text = "Substrate", variable = isPID_Option_Value, value = True)
    PID_Option_Substrate.place(x = 410, y = 150)
    
    PID_Option_TopPlate = Radiobutton(root, text = "Top Plate", variable = isPID_Option_Value, value = False)
    PID_Option_TopPlate.place(x = 410, y = 200)

    #Run Stop Button
    isRunning = BooleanVar()

    Start_Button = Button(root, text = "Start",  command = on, fg = "black", bd = 3, bg = "light green", font=fbody)
    Start_Button.place(x = 500, y = 250)

    Stop_Button = Button(root, text = "Stop", command = off, fg = "black", bd = 3, bg = "red", font = fbody)
    Stop_Button.place(x = 410, y = 250)

    #start and stop recording
    Start_Data_Button = Button(root, text = "Start Recording",  command = data_on, fg = "black", bd = 3, bg = "light green", font=fbody)
    Start_Data_Button.place(x = 550, y = 350)

    Stop_Data_Button = Button(root, text = "Stop recording", command = data_off, fg = "black", bd = 3, bg = "red", font = fbody)
    Stop_Data_Button.place(x = 420, y = 350)

    Save_Data_Button = Button(root, text = "Save Data", command = data_save, fg = "black", bd = 3, bg = "blue", font = fbody)
    Save_Data_Button.place(x = 310, y = 350)

    Save_Label = Label(root, text = "Enter your data name:", font = fbody)
    Save_Label.place(x = 250, y = 450)
    Save_name = Entry(root, bd = 3)
    Save_name.place(x = 420, y = 450)
    Save_name.insert(0,'###')
    #Submit Button
    Submit = Button(root, text = "Submit", command = set_state, font = fbody)
    Submit.place(x = 10, y = 250)

    



    get_state() #this should run every loop
    #Loops the above script. any lines past this point will not be executed
    #Mainloop is a default options and is actually seen as bad practice. and should be replaced eventually.
    root.mainloop()
q = Queue()
gui_start(q)