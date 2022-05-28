from calendar import month
from tkinter import *
import tkinter as tk
from tkcalendar import DateEntry
w = tk.Tk()
w.geometry("350x100") 
font1=('Times',18,'bold')	

sel = tk.StringVar()
def show_date():
    print(sel.get())
        
def getDataEntry(my_w):

    cal = DateEntry(my_w, selectmode="day", date_pattern='dd/mm/y', textvariable=sel)
    cal.grid(row=1, column=1, padx=15)
    sel.trace("w", show_date)

getDataEntry(w)
w.mainloop()  # Keep the window open