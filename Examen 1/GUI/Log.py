from tkinter import messagebox

def showError(message:str):
    messagebox.showerror("Error", message)

def showInfo(message:str):
    messagebox.showinfo("Información", message)