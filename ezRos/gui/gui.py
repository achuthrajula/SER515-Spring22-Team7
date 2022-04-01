from random import uniform
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import os
from _root_path import ROOT_DIRECTORY


class GUI():
    def __init__(self) -> None:
        pass
    def gui(self):
        window =Tk()
        window.title("ezRos")
        window.geometry("300x300")


        def about():
            messagebox.showinfo('ezRos', '  An object oriented approach to make ROS2 implementation easier')

        def open_sensors():
            sensorwindow = Toplevel(window)

            sensorwindow.title("Select the sensor to mount")

            sensorwindow.geometry("200x200")

            def click(count):
                os.system(f"gazebo --verbose {ROOT_DIRECTORY}/Gazebo-Worlds/4_{count}_x_alpha_gazebo_environment.world")

            Grid.rowconfigure(sensorwindow,0,weight=1)
            Grid.columnconfigure(sensorwindow,0,weight=1)
 
            Grid.rowconfigure(sensorwindow,1,weight=1)
            Grid.columnconfigure(sensorwindow,1,weight=0)

            Grid.rowconfigure(sensorwindow,2,weight=1)
            Grid.columnconfigure(sensorwindow,1,weight=0)

            Nosensors = tk.Button(sensorwindow, text = "No sensors",bg="#DADAE6", command = lambda: click(0))
            Nosensors.grid(row = 0, column = 0, columnspan=2, sticky="NSEW",ipadx=50,ipady=50)
 
            laser = tk.Button(sensorwindow, text = "Laser", bg="#007FFF", command = lambda: click(1))
            laser.grid(row = 1, column = 0, sticky="NSEW",ipadx=50,ipady=50)
 
            camera = tk.Button(sensorwindow, text = "Camera", bg="#F6D55C",command = lambda: click(2))
            camera.grid(row = 2, column = 0, sticky="NSEW",ipadx=50,ipady=50)

            camlaser = tk.Button(sensorwindow, text = "Camera and Laser",  bg="#38a500", width=12, command = lambda: click(3))
            camlaser.grid(row = 1, column = 1, rowspan=2, sticky="NSEW")

            close = tk.Button(sensorwindow, text="Close", bg="red",command=sensorwindow.destroy)
            close.grid(row=3,column=0,columnspan=2,sticky="NSEW")

            sensorwindow.mainloop()


        menubar = Menu(window, background='#0b91a3', foreground='black', activebackground='#10adc2', activeforeground='white')  
        file = Menu(menubar)  
        file.add_command(label="New")  
        file.add_command(label="Open")  
        file.add_command(label="Save")  
        file.add_command(label="Save as")    
        file.add_separator()  
        file.add_command(label="Exit", command=window.quit)  
        menubar.add_cascade(label="File", menu=file)  

        edit = Menu(menubar, tearoff=0)  
        edit.add_command(label="Undo")  
        edit.add_separator()     
        edit.add_command(label="Cut")  
        edit.add_command(label="Copy")  
        edit.add_command(label="Paste")  
        menubar.add_cascade(label="Edit", menu=edit)  

        help = Menu(menubar, tearoff=0)  
        help.add_command(label="About", command=about)  
        menubar.add_cascade(label="Help", menu=help)  
            
        sensors = Menu(menubar, tearoff=0)

        sensors.add_command(label="Select the type of sensor", command= open_sensors)
        menubar.add_cascade(label = "Sensors",menu = sensors)

        window.config(menu=menubar)
        window.mainloop()
        