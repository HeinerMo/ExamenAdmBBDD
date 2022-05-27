from tkinter import Label as tkLabel, Tk

class Label:
    def __init__(self, window:Tk):
        self.__label = tkLabel(window)

    def setPosition(self, posX:int=0, posY:int=0):
        self.__label.place(x=posX, y=posY)

    def setText(self, title:str):
        self.__label['text'] = title

    def setBackgroundColor(self, color:str):
        self.__label["bg"] = color

    def setForegroundColor(self, color:str):
        self.__label["fg"] = color

    def grid(self, pRow:int = 0, pColumn:int = 1, pPady:int = 5, pPadx:int = 5):
        self.__label.grid(row = pRow, column = pColumn, padx = pPadx, pady = pPady)

    def setSize(self, width:int=300, height:int=200):
        self.__label.config(height=height, width=width)