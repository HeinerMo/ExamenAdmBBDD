from operator import mod
from tkinter import Tk
from Button import Button
from Label import Label
from TextField import TextField

class Window():
    def __init__(self):
        self.__window=Tk()

    def startWin(self):
        self.__window.mainloop()

    def defaultInit(self):
        self.setTitle()
        self.setBounds()
        self.__window.mainloop()

    def setTitle(self, title:str="Default Title"):
        self.__window.title(title)
    
    def setBounds(self, posX:int=0, posY:int=0, width:int=300, height:int=200):
        self.__window.geometry(str(width)+"x"+str(height)+"+"+str(posX)+"+"+str(posY))

    def setLocation(self, posX:int, posY:int):
        self.__window.geometry("+"+str(posX)+"+"+str(posY))

    def setSize(self, width:int=300, height:int=200):
        self.__window.geometry(str(width)+"x"+str(height))

    def setLocationCenter(self):
        windowWidth = self.__window.winfo_reqwidth()
        windowHeight = self.__window.winfo_reqheight()
        posX = int(self.__window.winfo_screenwidth()/2 - windowWidth) - windowWidth
        posY = int(self.__window.winfo_screenheight()/2 - windowHeight) - windowHeight
        self.setLocation(posX, posY)

    def destroy(self):
        self.__window.destroy()

    def getWindow(self):
        return self.__window

    def createButton(self):
        btn=Button(self.__window)
        btn.setPosition(0, 0)
        return btn

    def createLabel(self):
        lbl=Label(self.__window)
        lbl.setPosition(0,0)
        return lbl

    def createTextField(self):
        txt=TextField(self.__window)
        txt.setPosition(0, 0)
        return txt

    def onTop(self):
        self.__window.wm_attributes("-topmost", 1)
