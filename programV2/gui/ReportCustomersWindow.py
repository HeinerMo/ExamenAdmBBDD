from gui.components.Window import Window
from util.SSConection import PySSAdmin
import util.Log as Log
import util.Util as Util
import pyodbc
from gui.ReportAPC import ReportAPC

class ReportCustomersWindow (Window):
    def __init__(self, ssConn:PySSAdmin):
        Window.__init__(self)
        self.ssConn = ssConn
        self.onTop()
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
        lblClient.setPosition(300, 400)

        self.txtClient = self.createTextField()
        self.txtClient.setSize(100, 20)
        self.txtClient.setPosition(275, 430)

        lblId = self.createLabel()
        lblId.setText("Customer ID")
        lblId.setBackgroundColor("white")
        lblId.setPosition(400, 400)

        self.txtId = self.createTextField()
        self.txtId.setSize(100, 20)
        self.txtId.setPosition(400, 430)

        lblState = self.createLabel()
        lblState.setText("Eliminado")
        lblState.setBackgroundColor("white")
        lblState.setPosition(400, 330)

        self.txtState = self.createTextField()
        self.txtState.setSize(100, 20)
        self.txtState.setPosition(400, 360)

        btnGen = self.createButton()
        btnGen.setText("Generar Reporte")
        btnGen.setBackgroundColor("#004972")
        btnGen.setForegroundColor("white")
        btnGen.setPosition(200, 470)
        btnGen.execMethod(self.onGenAction)

        btnMore = self.createButton()
        btnMore.setText("Más información del cliente seleccionado")
        btnMore.setBackgroundColor("#004972")
        btnMore.setForegroundColor("white")
        btnMore.setPosition(150, 270)
        btnMore.execMethod(self.moreInfo)

        self.tblTable = self.createTable()
        self.tblTable.setSize(300, 300)
        self.tblTable.pack()

    
    def onGenAction(self):
        isBeginDate = "NULL"
        isEndDate = "NULL"
        isLastName = "NULL"
        isName = "NULL"
        isClient = "NULL"
        isIdCust = "NULL"
        isDeleted = "NULL"

        beginDate = self.txtBeginDate.getText()[0:10]
        if (self.isValidDate(beginDate) and not beginDate.isspace() and not len(beginDate)==0):
            isBeginDate = "'"+beginDate+"'"

        endDate = self.txtEndDate.getText()[0:10]
        if (self.isValidDate(endDate) and not endDate.isspace() and not len(endDate)==0):
            isEndDate = "'"+endDate+"'"

        lastName = self.txtLastName.getText()
        if (not lastName.isspace() and not len(lastName)==0):
            isLastName = "'"+lastName+"'"

        name = self.txtName.getText()
        if (not name.isspace() and not len(name)==0):
            isName = "'"+name+"'"

        client = self.txtClient.getText()
        if (not client.isspace() and not len(client)==0):
            isClient = "'"+client+"'"

        idCust = self.txtId.getText()
        if (not idCust.isspace() and not len(idCust)==0):
            isIdCust = "'"+idCust+"'"

        idDeleted = self.txtState.getText()
        if (not idDeleted.isspace() and not len(idDeleted)==0):
            if (idDeleted != "0" and idDeleted != "1"):
                Log.showError("El estado del customer account debe ser 0 para eliminado o 1 para no eliminado")
            else:
                isDeleted = "'"+idDeleted+"'"

        try:
            query = "EXEC [dbo].[sp_CustomerAccounts] "+isBeginDate+", "+isEndDate+", "+isDeleted+", "+isClient+", "+isName+", "+isLastName+", "+isIdCust
            df = self.ssConn.tableToDataFrame(query)
            self.tblTable.insertDataFrame(df)
        except Exception as e:
            Log.showError("No se puede generar este reporte")
            self.destroy()
            return

    def moreInfo(self):
        isValid = len(self.tblTable.getSelectRow()['values']) > 0

        if (isValid):
            reportMore = ReportAPC(self.ssConn, self.tblTable.getSelectRow()['values'])
            reportMore.setSize(500, 500)
            reportMore.setTitle("Reporte de más información")
            reportMore.setLocation(self.getPosX(), self.getPosY())
    
    def isValidDate(self, date:str):
        return Util.isValidDate(date)

            

