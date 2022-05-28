from pydoc import isdata
from gui.components.Window import Window
from util.SSConection import PySSAdmin
import util.Log as Log
import util.Util as Util

class ReportTransactionsWindow (Window):
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

        lblTrancId = self.createLabel()
        lblTrancId.setText("Id de la Transacción")
        lblTrancId.setBackgroundColor("white")
        lblTrancId.setPosition(255,330)

        self.txtTrancId = self.createTextField()
        self.txtTrancId.setSize(100, 20)
        self.txtTrancId.setPosition(265,360)
        self.txtTrancId.maskText("*")

        lblMoney = self.createLabel()
        lblMoney.setText("Monto")
        lblMoney.setBackgroundColor("white")
        lblMoney.setPosition(0, 400)

        self.txtMoney = self.createTextField()
        self.txtMoney.setSize(100, 20)
        self.txtMoney.setPosition(0, 430)

        lblCurrrency = self.createLabel()
        lblCurrrency.setText("Moneda")
        lblCurrrency.setBackgroundColor("white")
        lblCurrrency.setPosition(150, 400)

        self.cmbCurrency = self.createComboBox()
        self.cmbCurrency.setSize(15, 5)
        self.cmbCurrency.setPosition(120, 430)
        self.cmbCurrency.setValues(["", ""])

        lblCustId = self.createLabel()
        lblCustId.setText("Id del CUSTOMER")
        lblCustId.setBackgroundColor("white")
        lblCustId.setPosition(245, 400)

        self.txtCustId = self.createTextField()
        self.txtCustId.setSize(100, 20)
        self.txtCustId.setPosition(265, 430)

        lblPayment = self.createLabel()
        lblPayment.setText("Tipo de pago")
        lblPayment.setBackgroundColor("white")
        lblPayment.setPosition(380, 400)

        self.cmbPayment = self.createComboBox()
        self.cmbPayment.setSize(15, 5)
        self.cmbPayment.setPosition(380, 430)
        self.cmbPayment.setValues(["", ""])

        lblClient = self.createLabel()
        lblClient.setText("Cliente")
        lblClient.setBackgroundColor("white")
        lblClient.setPosition(380, 330)

        self.cmbClient = self.createComboBox()
        self.cmbClient.setSize(15, 5)
        self.cmbClient.setPosition(380, 360)
        self.cmbClient.setValues(["", ""])

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

            

