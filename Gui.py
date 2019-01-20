# created with python 3
'''
Reminder: python 2 ~ from Tkinter import *
          python 3 ~ from tkinter import *
'''
from tkinter import *
master = Tk()

def callback():
    print("Click!")

b = Button(master, text="OK", command=callback)
b.pack()

mainloop()
