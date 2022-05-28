from tkinter import Tk
from tkinter.ttk import Entry as tkTextField

class TextField:
    def __init__(self, window:Tk):
        self.__textField = tkTextField(window)
        self.maskSymbol = ""

    def setPosition(self, posX:int=0, posY:int=0):
        self.__textField.place(x=posX, y=posY)

    def setText(self, title:str):
        self.__textField['text'] = title

    def setBackgroundColor(self, color:str):
        self.__textField["bg"] = color

    def setForegroundColor(self, color:str):
        self.__textField["fg"] = color

    def setSize(self, width:int=300, height:int=200):
        self.__textField.place(height=height, width=width)

    def maskText(self, symbol):
         self.__textField['show'] = symbol
         self.maskSymbol = symbol

    def formatText(self):
        self.__textField.formart

    def grid(self, pRow:int = 0, pColumn:int = 1, pPady:int = 5, pPadx:int = 5):
        self.__textField.grid(row = pRow, column = pColumn, padx = pPadx, pady = pPady)

    def getText(self):
        return self.__textField.get()

    """
    def setPlaceholder(self, text:str):
        self.placeholder = text
        self.__textField.insert("0", self.placeholder)
        self.__textField.bind("<FocusIn>", self._clear_placeholder)
        self.__textField.bind("<FocusOut>", self._add_placeholder)

    def _clear_placeholder(self, e):
        self.__textField.delete("0", "end")
        self.__textField['show'] = self.maskSymbol

    def _add_placeholder(self, e):
        if not self.__textField.get():
            self.__textField.insert("0", self.placeholder)
            self.__textField['show'] = "" """




#textbox.pack(pady=20)


