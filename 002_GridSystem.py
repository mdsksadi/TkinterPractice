from tkinter import *   #It will import everything from tkinter
root = Tk()

#Tkinet has 2 steps always. First defie the thing and then put it up into screen.

#Creating a Label Widget
myLable1 = Label(root,text="Hello World")
myLable2 = Label(root,text="My name is MD Shekh sadi")
myLable3 = Label(root,text="          ")

#Showing it onto the screen
#It is relative
myLable1.grid(row=0,column=0)   #This time if we resize the window, text will not change based on our resize.
myLable2.grid(row=1,column=5)   #This time if we resize the window, text will not change based on our resize.
myLable3.grid(row=1,column=1)


'''
######## It is also possible to do both step in a same line ########

myLable1 = Label(root,text="Hello World").grid(row=0,column=0)  
myLable2 = Label(root,text="My name is MD Shekh sadi").grid(row=0,column=0)  
myLable3 = Label(root,text="           ").grid(row=0,column=0)  

'''

#It will create a loop to run our code.
root.mainloop()