import sqlite3
from tkinter import *

def getTextInput():
    result=e1.get()
    print(result)

conn = sqlite3.connect('smit.db')
c = conn.cursor()

top = Tk()
top.geometry("400x250")

name=Label(top,text = 'Name').place(x = 30, y = 50)
email=Label(top,text = 'Email').place(x = 30, y = 90)
passsword=Label(top,text = 'password').place(x = 30, y = 130)
e1 = Entry(top).place(x = 80,y = 50)
e2 = Entry(top).place(x = 80,y = 90)
e3 = Entry(top).place(x = 80,y = 130)



btnRead=Button(top , height=1, width=10, text="submit",
                         command = getTextInput)

"""ur = conn.cursor()
print(c)
def create():
    sql = "create table if not exists user(id INTEGER PRIMARY KEY AUTOINCREMENT,\
    first_name TEXT NOT NULL,last_name TEXT)"
    print(sql)
    print(c.execute(sql))
"""
btnRead.pack()
top.mainloop()
#create()

