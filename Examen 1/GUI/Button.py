from tkinter import Button as tkButton, Tk

class Button:
    def __init__(self, window:Tk):
        self.__button = tkButton(window)
    
    def setPosition(self, posX:int=0, posY:int=0):
        self.__button.place(x=posX, y=posY)

    def setText(self, title:str):
        self.__button['text'] = title

    def setBackgroundColor(self, color:str):
        self.__button["bg"] = color

    def setForegroundColor(self, color:str):
        self.__button["fg"] = color

    def setSize(self, width:int=300, height:int=200):
        self.__button.config(height=height, width=width)

    def execMethod(self, method):
        self.__button["command"] = method