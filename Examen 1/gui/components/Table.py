from tkinter import Frame, Tk, Scrollbar, RIGHT, Y, BOTTOM, X, CENTER, NO, YES, BOTH
from tkinter import ttk
import pandas as pd

class Table():
    def __init__(self, window:Tk):
        self.frame = Frame(window)
        self.frame.pack()
        #scrollbar
        self.scrollBarY = Scrollbar(self.frame)
        self.scrollBarY.pack(side=RIGHT, fill=Y)

        self.scrollBarX = Scrollbar(self.frame, orient='horizontal')
        self.scrollBarX.pack(side= BOTTOM,fill=X)

        self.__treeView = ttk.Treeview(self.frame, selectmode="extended", yscrollcommand=self.scrollBarY.set, xscrollcommand=self.scrollBarX.set)

        self.scrollBarY.config(command=self.__treeView.yview)
        self.scrollBarX.config(command=self.__treeView.xview)
    
        self.__treeView.column("#0", width=0,  stretch=NO)
        self.__treeView.heading("#0",text="",anchor=CENTER)

        df = pd.read_csv('airlines_final.csv')
        self.insertDataFrame(df)

    def insertDataFrame(self, dataFrame:pd.DataFrame):
        for i in self.__treeView.get_children():
            self.__treeView.delete(i)

        self.__treeView["columns"] = dataFrame.columns.values.tolist()
        for x in range(len(dataFrame.columns.values)):
            self.__treeView.column(dataFrame.columns.values[x], width=100, stretch=False)
            self.__treeView.heading(dataFrame.columns.values[x], text=dataFrame.columns.values[x])

        for index, row in (dataFrame.loc[::-1]).iterrows():
            self.__treeView.insert("",0,text=index,values=list(row))

        self.frame.pack()

    def setPosition(self, posX:int=0, posY:int=0):
        self.frame.place(x=posX, y=posY)
        self.frame.pack()

    def setSize(self, width:int=300, height:int=200):
        self.frame.config(height=height, width=width)
        self.__treeView.pack()
        self.frame.pack()

    def pack(self):
        self.__treeView.pack()
        self.frame.pack()
"""
ws  = Tk()
ws.title('PythonGuides')
ws.geometry('500x500')
ws['bg'] = '#AC99F2'

tblTable = Table(ws)
tblTable.setPosition(0, 100)
tblTable.setSize(300, 300)

df = pd.read_csv('airlines_final.csv')

tblTable.insertDataFrame(df)

ws.mainloop()
"""