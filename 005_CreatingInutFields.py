from tkinter import *   #It will import everything from tkinter
root = Tk()

'''
Here 'e' is a variable. Entry is a function to create a box to take entry.
width is the width of the box
we can also set the text color and background color of the box by fg and bg.
borderwidth changes the borderwidth of the box
'''
e=Entry(root, width=50,fg="red", bg="gray", borderwidth=5)   
e.pack()
e.insert(0, "Enter your name: ")    #It will be initually incerted to the box. 0 is the index number.

def myClick():
    myLabel = Label(root, text="Hello "+e.get()) #.get function will take input from user. Here 'e' is our box.
    myLabel.pack()

myButton = Button(root,text="Enter Your Name", command=myClick) #No need to use () to call a function here.

#Showing it onto the screen
myButton.pack()


#It will create a loop to run our code.
root.mainloop()