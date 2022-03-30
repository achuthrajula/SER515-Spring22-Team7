from tkinter import *
from tkinter import messagebox

class GUI():
    def __init__(self) -> None:
        pass

    def gui(self):

        def about():
            messagebox.showinfo('ezRos', 'Python Guides aims at providing best practical tutorials')

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
            
        window.config(menu=menubar)
        window.mainloop()

        