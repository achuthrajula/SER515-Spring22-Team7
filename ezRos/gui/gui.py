from tkinter import *
from tkinter import messagebox

class GUI():
    def __init__(self) -> None:
        self.sensor_input= 0

    def gui(self):

        def about():
            messagebox.showinfo('ezRos', '  An object oriented approach to make ROS2 implementation easier')

        
        def laser():
            self.sensor_input = 1
        
        def camera():
            self.sensor_input = 2

        def camlaser():
            self.sensor_input = 3

        window =Tk()
        window.title("ezRos")
        window.geometry("300x300")

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
        sensors.add_command(label="No sensors")
        sensors.add_command(label="Laser",command=laser)
        sensors.add_command(label="Camera",command=camera)
        sensors.add_command(label="Camera and Laser",command=camlaser)
        menubar.add_cascade(label = "Sensors",menu = sensors)

        window.config(menu=menubar)
        window.mainloop()

        