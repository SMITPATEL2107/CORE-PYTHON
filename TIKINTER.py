    from tkinter import *

"""
1.import the tinker module..
2.create main application window..
3.add the widget like lables,buttons, etc to the window..
4.call the main event loop so that the action can take place on the 
   user's computer screen...
"""

top = Tk()
greeting = Label(
    text="hello tkinter",
    foreground ="white", #set of text colour to white
    background ="black" #set of background colour to black
    )

#use 3 function for show widget on screen
#1.
#greeting.pack(side=RIGHT) #TOP,LEFT,BOTTOM 

#2.
#greeting.grid(row=0,column=1)

#3.
#greeting.place(x = 30,y = 50)

#top.geometry("400x250")

# x,y It refers to the horizontal and vertical offset in the pixel
"""name=Label(top,text = 'Name').place(x = 30, y = 50)
email=Label(top,text = 'Email').place(x = 30, y = 90)
passsword=Label(top,text = 'password').place(x = 30, y = 130)
e1 = Entry(top).place(x = 80,y = 50)
e2 = Entry(top).place(x = 80,y = 90)
e3 = Entry(top).place(x = 80,y = 130)

top.mainloop()#creting new window for GUI
"""

import tkinter as tk
root=tk.Tk()
#root.geomerty("400x240")

def getTextInput():
    result=entry.get()
    print(result)

entry=tk.Entry(root)
entry.pack()
btnRead=tk.Button(root, height=1, width=10, text="Read",
                         command = getTextInput)

btnRead.pack()
root.mainloop()


