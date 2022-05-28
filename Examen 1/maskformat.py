from ctypes import sizeof
from tkinter import *
import tkinter as tk
my_w = tk.Tk()
my_w.geometry("350x100") 
font1=('Times',18,'bold')	


splitSymbol = "/"
year = ""
day = ""
month = ""

def show_format(*args):
    position = e1.index(INSERT) # getting cursor position
    if(position == 4 or position == 7):
        e1_str.set(e1.get() + splitSymbol)
        e1.icursor(position+1) # shift cursor one position

    if (position == 4):
            print(e1.get().split(splitSymbol)[0])
    if (position == 7):
        print(e1.get().split(splitSymbol)[1])
    if (position == 10):
        print(e1.get().split(splitSymbol)[2])
    
    if (position >= 11):
        begin = len(e1.get())
        e1.delete(begin-1, begin)
    
        


  
e1_str=tk.StringVar() # string variable   
e1 = tk.Entry(my_w,font=font1,width=20,textvariable=e1_str)
e1.grid(row=1,column=1,padx=18,pady=5)
#e1.bind("<FocusOut>",show_format) # when tab is pressed
e1.bind("<KeyRelease>",show_format) # when key is released


my_w.mainloop()  # Keep the window open