
"""
# import package_name as alias
# this helps save typing while preserving namespace
# functions and classes
"""
# import our model functions
import zhu as z
# import the GUI library
import tkinter as tk


"""
How to get help in python
dir(z) # This displays all the classes and functions in zhu module
help(z) # This displays all the information about the z package
print(z.__doc__) # This displays the documentation for your package if there are any
dir(tk)
help(tk)
print(tk.__doc__)
"""

"""
Creating the GUI
"""
if __name__ == "__main__" : 
# m is the main window object
    m = tk.Tk()
    m.title('Signal Processor Control System') 

# Code to add widgets will go here

    tk.Label(m, text='Address').grid(row=0) 
    tk.Label(m, text='Burst Length').grid(row=1) 
    tk.Label(m, text='Write Data').grid(row=2) 
    tk.Label(m, text='Save As').grid(row=2) 
    w1 = tk.Entry(m) 
    w2 = tk.Entry(m) 
    w3 = tk.Entry(m) 
    w1.grid(row=0,column=1)
    w2.grid(row=1,column=1)
    w3.grid(row=2,column=1)
# w1.pack()
# w2.pack()
# w3.pack()

# mainWindowTitle = tk.Label(m, text=z.helloworld())
# mainWindowTitle.pack()
# button = tk.Button(m, text='Stop', width=25, command=m.destroy) 

# Start the GUI
    m.mainloop()

