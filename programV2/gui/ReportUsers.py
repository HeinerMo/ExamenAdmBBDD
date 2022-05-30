from pydoc import isdata
from gui.components.Window import Window
from util.SSConection import PySSAdmin
import util.Log as Log
import util.Util as Util
import pandas as pd
from tkinter import ttk
import tkinter as tk
import pyodbc

class ReportUsers (Window):
    def __init__(self, ssConn:PySSAdmin):
        Window.__init__(self)
        self.ssConn = ssConn
        self.initComponents()

    def initComponents(self):

        lblName = self.createLabel()
        lblName.setText("Nombre de Usuario")
        lblName.setBackgroundColor("white")
        lblName.setPosition(0, 400)

        self.txtName = self.createTextField()
        self.txtName.setSize(100, 20)
        self.txtName.setPosition(0, 430)

        lblPerRead = self.createLabel()
        lblPerRead.setText("Permiso de Lectura")
        lblPerRead.setBackgroundColor("white")
        lblPerRead.setPosition(150, 340)

        self.cmbPerRead = self.createComboBox()
        self.cmbPerRead.setSize(15, 5)
        self.cmbPerRead.setPosition(120, 370)
        self.cmbPerRead.setValues(["", "Tiene Lectura", "No tiene Lectura"])
        
        lblPerUser = self.createLabel()
        lblPerUser.setText("Permiso de Usuarios")
        lblPerUser.setBackgroundColor("white")
        lblPerUser.setPosition(150, 400)

        self.cmbPerUser = self.createComboBox()
        self.cmbPerUser.setSize(15, 5)
        self.cmbPerUser.setPosition(120, 430)
        self.cmbPerUser.setValues(["", "Agrega Usuarios", "No Agrega Usuarios"])

        lblState = self.createLabel()
        lblState.setText("Estado")
        lblState.setBackgroundColor("white")
        lblState.setPosition(300, 400)

        self.cmbState = self.createComboBox()
        self.cmbState.setSize(15, 5)
        self.cmbState.setPosition(275, 430)
        self.cmbState.setValues(["", "Activo", "Inactivo"])

        btnGen = self.createButton()
        btnGen.setText("Generar Reporte")
        btnGen.setBackgroundColor("#004972")
        btnGen.setForegroundColor("white")
        btnGen.setPosition(400, 430)
        btnGen.execMethod(self.onGenAction)

        self.tblTable = self.createTable()
        self.tblTable.setSize(300, 300)
        self.tblTable.pack()
    
    def onGenAction(self):
        isName = "NULL"
        canRead = "NULL"
        canAddUser = "NULL"
        isState = "NULL"
        
        if (not len(self.cmbPerRead.getSelection())==0):
            if (self.cmbPerRead.getSelection()=="Tiene Lectura"):
                canRead = "1"
            if (self.cmbPerRead.getSelection()=="No tiene Lectura"):
                canRead = "0"

        if (not len(self.cmbPerUser.getSelection())==0):
            if (self.cmbPerUser.getSelection()=="Agrega Usuarios"):
                canAddUser = "1"
            if (self.cmbPerUser.getSelection()=="No Agrega Usuarios"):
                canAddUser = "0"

        if (not len(self.cmbState.getSelection())==0):
            if (self.cmbState.getSelection()=="Activo"):
                isState = "1"
            if (self.cmbState.getSelection()=="Inactivo"):
                isState = "0"

        userName = self.txtName.getText()
        if (not userName.isspace() and not len(userName)==0):
            isName = "'"+userName+"'"       

        try:
            query = "EXEC [dbo].[sp_Users] "+isName+", "+canRead+", "+canAddUser+", "+isState
            #cursor = self.ssConn.getCursor().execute(query)
            df = self.ssConn.tableToDataFrame(query)
            self.tblTable.insertDataFrame(df)      
            #cursor.commit()
        except Exception as e:
            Log.showError("No se puede generar este reporte")
            self.destroy()
            return

            

