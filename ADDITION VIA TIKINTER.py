from tkinter import *
import tkinter as tk
root=tk.Tk()
#root.geomerty("400x240")

def getTextInput():
    result=int(entry.get())
    re=int(entry1.get())
    print(result+re)

entry=tk.Entry(root)
entry.pack()

entry1=tk.Entry(root)
entry1.pack()


btnRead=tk.Button(root, height=1, width=10, text="Read",
                         command = getTextInput)

btnRead.pack()
root.mainloop()