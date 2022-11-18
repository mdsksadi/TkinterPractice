from tkinter import *   #It will import everything from tkinter
root = Tk()

#Tkinet has 2 steps always. First defie the thing and then put it up into screen.

#Creating a Label Widget
myLable1 = Label(root,text="Hello World")

#Shoving it onto the screen
myLable1.pack()

#It will create a loop to run our code.
root.mainloop()