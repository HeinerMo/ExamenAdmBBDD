from pydoc import isdata
from gui.components.Window import Window
from util.SSConection import PySSAdmin
import util.Log as Log
import util.Util as Util
import pandas as pd
from tkinter import ttk
import tkinter as tk
import pyodbc

class ReportAPC (Window):
    def __init__(self, ssConn:PySSAdmin, clientData:list):
        Window.__init__(self)
        self.ssConn = ssConn
        self.clientData = clientData
        self.onTop()
        self.initComponents()

    def initComponents(self):

        lblName = self.createLabel()
        lblName.setText(f"Nombre de Usuario: {self.clientData[2]}                            Customer Id: {self.clientData[0]}")
        lblName.setBackgroundColor("white")
        lblName.setPosition(0, 400)

        btnAddress = self.createButton()
        btnAddress.setText("Ver direcciones") 
        btnAddress.setBackgroundColor("#004972")
        btnAddress.setForegroundColor("white")
        btnAddress.setPosition(0, 430)
        btnAddress.execMethod(self.onAddressAction)

        btnPhones = self.createButton()
        btnPhones.setText("Ver telefonos") 
        btnPhones.setBackgroundColor("#004972")
        btnPhones.setForegroundColor("white")
        btnPhones.setPosition(120, 430)
        btnPhones.execMethod(self.onPhonesAction)
        
        btnCard = self.createButton()
        btnCard.setText("Ver Tarjetas de Crédito")
        btnCard.setBackgroundColor("#004972")
        btnCard.setForegroundColor("white")
        btnCard.setPosition(275, 430)
        btnCard.execMethod(self.onCardAction)

        self.tblTable = self.createTable()
        self.tblTable.setSize(300, 300)
        self.tblTable.pack()
    
    def onAddressAction(self):  
        try:
            query = "EXEC [dbo].[sp_Address] "+str(self.clientData[0])
            df = self.ssConn.tableToDataFrame(query)
            self.tblTable.insertDataFrame(df)      

        except Exception as e:
            Log.showError("No se puede generar este reporte")
            self.destroy()
            return
    
    def onPhonesAction(self):  
        try:
            query = "EXEC [dbo].[sp_Phones] "+str(self.clientData[0])
            df = self.ssConn.tableToDataFrame(query)
            self.tblTable.insertDataFrame(df)      

        except Exception as e:
            Log.showError("No se puede generar este reporte")
            self.destroy()
            return

    def onCardAction(self):  
        try:
            query = "EXEC [dbo].[sp_CreditCard] "+str(self.clientData[0])
            df = self.ssConn.tableToDataFrame(query)
            self.tblTable.insertDataFrame(df)      

        except Exception as e:
            Log.showError("No se puede generar este reporte")
            self.destroy()
            return

            

