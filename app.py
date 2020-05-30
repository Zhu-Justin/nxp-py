# import the GUI library
import tkinter as tk
# import our model functions
import zhu as z

dir(z)
print(z.helloworld())

# m is the main window object
# m = tk.Tk()
# Code to add widgets will go here...

mainWindowTitle = tk.Label(m, text="Our New GUI Hi")
mainWindowTitle.pack()
m.mainloop()

# mainWindow = Tk()
# mainWindowTitle = Label(mainWindow, text="Our New GUI")
# mainWindowTitle.pack()
# mainWindow.mainloop()

