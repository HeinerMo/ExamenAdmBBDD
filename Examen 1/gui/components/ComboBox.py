from tkinter import ttk, Tk

class ComboBox:
    def __init__(self, window:Tk):
        self.__comboBox = ttk.Combobox(window,  state="readonly")
    
    def setPosition(self, posX:int=0, posY:int=0):
        self.__comboBox.place(x=posX, y=posY)

    def setValues(self, values:list[str]):
        self.__comboBox['values'] = values

    def setBackgroundColor(self, color:str):
        self.__comboBox["bg"] = color

    def setForegroundColor(self, color:str):
        self.__comboBox["fg"] = color

    def setSize(self, width:int=300, height:int=200):
        self.__comboBox.config(height=height, width=width)

    def grid(self, pRow:int = 0, pColumn:int = 1, pPady:int = 5, pPadx:int = 5):
        self.__comboBox.grid(row = pRow, column = pColumn, padx = pPadx, pady = pPady)

    def getSelection(self):
        return self.__comboBox.get()

    def getComboBox(self):
        return self.__comboBox

    def setState(self, state:str):
        self.__comboBox.state = state
        