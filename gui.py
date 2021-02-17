#Imports
from tkinter import *
from tkinter import font
#import matplotlib.pyplot as plt
#import matplotlib


#Defining Class
class system_state:
  def init (self, run, temp, subthermoexist, controllocation, setpoint,time_pid):
    self.run = False #are we running the system
    self.temp = [0,0,0,0,0,0,0,0,0,0,0,0,0] #temperature array, thermos 1-13
    self.subthermoexist= False #Does the Substrate thermocouple exist
    self.controllocation = True #PID from the bed(false) or substrate (true)
    self.setpoint = 400    #temp setpoint
    self.time_pid = time.time()
    return

#Defines an object of class system_state
Currentstate=system_state()

#==================== Back End
Time_pid_stored=0
temp_stored=[0,0,0,0,0,0,0,0,0,0,0,0,0]
#Retrieve updates currentstate object
def graph():
    temp_stored=temp_stored.append+Currentstate.temp
    Time_pid_stored=Time_pid_stored.append+Currentstate.time_pid
    #ax.plot(xdata1, ydata1, color='tab:blue')
    #ax.plot(xdata2, ydata2, color='tab:orange')
    #plt.ylabel('Temperature, C')
    #plt.xlabel('Time, s')
    #plt.show()
    #counter=counter+1
def retrieve():
    Currentstate.subthermoexist = isSubstrate_Thermocouple_Value
    Currentstate.controllocation = isPID_Option_Value
    Currentstate.setpoint = Temp_Set
    Currentstate.run = isRunning
    


    
#Functions for on and off buttons; updates retrieve
def on():
    isRunning = True
    retrieve()
def off():
    isRunning = False
    retrieve()

#Now we get into tkinter
#Defines overall box
root = Tk()
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


#Submit Button
Submit = Button(root, text = "Submit", command = retrieve, font = fbody)
Submit.place(x = 10, y = 250)




#Loops the above script. any lines past this point will not be executed
#Mainloop is a default options and is actually seen as bad practice. and should be replaced eventually.
root.mainloop()
