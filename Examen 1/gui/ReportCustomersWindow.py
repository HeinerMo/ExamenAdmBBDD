from pydoc import isdata
from gui.components.Window import Window
from util.SSConection import PySSAdmin
import util.Log as Log
import util.Util as Util

class ReportCustomersWindow (Window):
    def __init__(self, ssConn:PySSAdmin):
        Window.__init__(self)
        self.ssConn = ssConn
        self.initComponents()

    def initComponents(self):

        lblBeginDate = self.createLabel()
        lblBeginDate.setText("Fecha de Inicio")
        lblBeginDate.setBackgroundColor("white")
        lblBeginDate.setPosition(0,330)

        self.txtBeginDate = self.createTextField()
        self.txtBeginDate.setSize(100, 20)
        self.txtBeginDate.setPosition(0,360)

        lblEndDate = self.createLabel()
        lblEndDate.setText("Fecha de Fin")
        lblEndDate.setBackgroundColor("white")
        lblEndDate.setPosition(130,330)

        self.txtEndDate = self.createTextField()
        self.txtEndDate.setSize(100, 20)
        self.txtEndDate.setPosition(120,360)

        lblLastName = self.createLabel()
        lblLastName.setText("Apellido")
        lblLastName.setBackgroundColor("white")
        lblLastName.setPosition(280,330)

        self.txtLastName = self.createTextField()
        self.txtLastName.setSize(100, 20)
        self.txtLastName.setPosition(265,360)
        self.txtLastName.maskText("*")

        lblName = self.createLabel()
        lblName.setText("Nombre")
        lblName.setBackgroundColor("white")
        lblName.setPosition(0, 400)

        self.txtName = self.createTextField()
        self.txtName.setSize(100, 20)
        self.txtName.setPosition(0, 430)

        lblClient = self.createLabel()
        lblClient.setText("Cliente")
        lblClient.setBackgroundColor("white")
        lblClient.setPosition(150, 400)

        self.cmbClient = self.createComboBox()
        self.cmbClient.setSize(15, 5)
        self.cmbClient.setPosition(120, 430)
        self.cmbClient.setValues([""])

        lblPhone = self.createLabel()
        lblPhone.setText("Telefono")
        lblPhone.setBackgroundColor("white")
        lblPhone.setPosition(300, 400)

        self.txtPhone = self.createTextField()
        self.txtPhone.setSize(100, 20)
        self.txtPhone.setPosition(275, 430)

        lblId = self.createLabel()
        lblId.setText("ID")
        lblId.setBackgroundColor("white")
        lblId.setPosition(400, 400)

        self.txtId = self.createTextField()
        self.txtId.setSize(100, 20)
        self.txtId.setPosition(400, 430)

        lblAddress = self.createLabel()
        lblAddress.setText("Dirección")
        lblAddress.setBackgroundColor("white")
        lblAddress.setPosition(400, 330)

        self.txtAddress = self.createTextField()
        self.txtAddress.setSize(100, 20)
        self.txtAddress.setPosition(400, 360)

        btnGen = self.createButton()
        btnGen.setText("Generar Reporte")
        btnGen.setBackgroundColor("#004972")
        btnGen.setForegroundColor("white")
        btnGen.setPosition(200, 470)
        btnGen.execMethod(self.onGenAction)

        self.tblTable = self.createTable()
        self.tblTable.setSize(300, 300)
        self.tblTable.pack()

    
    def onGenAction(self):
        isBeginDate = False
        isEndDate = False

        beginDate = self.txtBeginDate.getText()[0:10]
        if (self.isValidDate(beginDate) and not beginDate.isspace() and not len(beginDate)==0):
            isBeginDate = True

        endDate = self.txtEndDate.getText()[0:10]
        if (self.isValidDate(endDate) and not endDate.isspace() and not len(endDate)==0):
            isEndDate = True

        if (not isEndDate and isBeginDate):
            Log.showError("""Debe ingresar una Fecha de Fin con el siguiente formato: yyyy-mm-dd. O deje ambos espacios en blanco si no desea ingresar fechas.""")
        
        if (not isBeginDate and isEndDate):
            Log.showError("""Debe ingresar una Fecha de Inicio con el siguiente formato: yyyy-mm-dd. O deje ambos espacios en blanco si no desea ingresar fechas.""")
        
    
    def isValidDate(self, date:str):
        return Util.isValidDate(date)

            

