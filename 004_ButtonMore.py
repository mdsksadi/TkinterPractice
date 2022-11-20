from tkinter import *   #It will import everything from tkinter
root = Tk()

def myClick():
    myLabel = Label(root, text="Look! I clicked a Button!!!")
    myLabel.pack()
'''
padx is the x axis length of button
pady is the y axis length of button
state = DISABLED works to disable the button
fg means forget color. It changes the text color of the button
bg means background color. It changes the bakground color of the button.
I can also use #FFFFFF type hex color code
'''
myButton = Button(root,text="Click Me!", padx=50, pady=40, command=myClick, fg="blue", bg="gray") #No need to use () to call a function here.

#Showing it onto the screen
myButton.pack()


#It will create a loop to run our code.
root.mainloop()