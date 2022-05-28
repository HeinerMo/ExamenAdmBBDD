from pydoc import isdata
from gui.components.Window import Window
from util.SSConection import PySSAdmin
import util.Log as Log
import util.Util as Util
import pandas as pd
from tkinter import ttk
import tkinter as tk

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

        lblPermission = self.createLabel()
        lblPermission.setText("Permiso")
        lblPermission.setBackgroundColor("white")
        lblPermission.setPosition(150, 400)

        self.cmbPermission = self.createComboBox()
        self.cmbPermission.setSize(15, 5)
        self.cmbPermission.setPosition(120, 430)
        self.cmbPermission.setValues(["", "Agregar Usuarios", "Lectura"])

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

        isName = False
        isPermission = False
        isState = False

        if (not len(self.cmbPermission.getSelection())==0):
            isPermission = True

        if (not len(self.cmbState.getSelection())==0):
            isState = True

        df = pd.read_csv('airlines_final.csv')
        self.tblTable.insertDataFrame(df)      
    
    def isValidDate(self, date:str):
        return Util.isValidDate(date)

            

