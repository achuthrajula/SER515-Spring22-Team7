from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
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

        def nolaser():
            os.system(f"gazebo --verbose {ROOT_DIRECTORY}/Gazebo-Worlds/4_0_x_alpha_gazebo_environment.world")

        def laser():
            os.system(f"gazebo --verbose {ROOT_DIRECTORY}/Gazebo-Worlds/4_1_x_alpha_gazebo_environment.world")
        
        def camera():
            os.system(f"gazebo --verbose {ROOT_DIRECTORY}/Gazebo-Worlds/4_2_x_alpha_gazebo_environment.world")

        def camlaser():
            os.system(f"gazebo --verbose {ROOT_DIRECTORY}/Gazebo-Worlds/4_3_x_alpha_gazebo_environment.world")


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
        sensors.add_command(label="No sensors",command=nolaser)
        sensors.add_command(label="Laser",command=laser)
        sensors.add_command(label="Camera",command=camera)
        sensors.add_command(label="Camera and Laser",command=camlaser)
        menubar.add_cascade(label = "Sensors",menu = sensors)

        window.config(menu=menubar)
        window.mainloop()

        