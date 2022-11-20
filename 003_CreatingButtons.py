from tkinter import *   #It will import everything from tkinter
root = Tk()

#Creating a Label Widget
#myButton = Button(root,text="Click Me!",state=DISABLED, padx=50,pady=40)

'''
padx is the x axis length of button
pady is the y axis length of button
state = DISABLED works to disable the button
'''
myButton = Button(root,text="Click Me!", padx=50, pady=40)  

#Showing it onto the screen
myButton.pack()


#It will create a loop to run our code.
root.mainloop()