from gui.components.Window import Window
from util.SSConection import PySSAdmin
import util.Log as Log
import util.Util as Util
import pyodbc
import pandas as pd

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

        try:
            selectCurrency = """SELECT
                [CURRENCY_ID]
                ,[CURRENCY_NAME]
                FROM [TRANSACTION_PROCESSING_EXAMEN].[FINANCIAL_DEPOSIT].[tb_CURRENCY]"""
            currencyTable = self.ssConn.tableToDataFrame(selectCurrency)
        except Exception as e:
            Log.showError("No se puede generar este reporte")
            self.destroy()
            return
        
        currencyNames:list[str] = [] 
        currencyNames.append("")
        self.currencyIndices:list[int]  = []
        self.currencyIndices.append(-1)
        for x in range(len(currencyTable)):
            currencyNames.append(currencyTable.iat[x,1])
            self.currencyIndices.append(currencyTable.iat[x,0])
        
        self.cmbCurrency = self.createComboBox()
        self.cmbCurrency.setSize(15, 5)
        self.cmbCurrency.setPosition(120, 430)
        self.cmbCurrency.setValues(currencyNames)

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

        try:
            selectPayment = """SELECT 
                                    [PAYMENT_TYPE_ID]
                                    ,[PAYMENT_TYPE]
                                FROM [TRANSACTION_PROCESSING_EXAMEN].[FINANCIAL_DEPOSIT].[tb_PAYMENT_TYPE]"""
            paymentTable = self.ssConn.tableToDataFrame(selectPayment)
        except Exception as e:
            Log.showError("No se puede generar este reporte")
            self.destroy()
            return
        
        paymentNames:list[str] = []
        paymentNames.append("")
        self.paymentIndices:list[int]  = []
        self.paymentIndices.append(-1)
        for x in range(len(paymentTable)):
            paymentNames.append(paymentTable.iat[x,1])
            self.paymentIndices.append(paymentTable.iat[x,0])

        self.cmbPayment = self.createComboBox()
        self.cmbPayment.setSize(15, 5)
        self.cmbPayment.setPosition(380, 430)
        self.cmbPayment.setValues(paymentNames)

        lblClient = self.createLabel()
        lblClient.setText("Cliente")
        lblClient.setBackgroundColor("white")
        lblClient.setPosition(380, 330)

        self.txtClient = self.createTextField()
        self.txtClient.setSize(100, 20)
        self.txtClient.setPosition(380, 360)

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
        isBeginDate = "NULL"
        isEndDate = "NULL"
        isIdTransac = "NULL"
        isClient = "NULL"
        isAmount = "NULL"
        isCurrency = "NULL"
        isIdCust = "NULL"
        isPayment = "NULL"

        beginDate = self.txtBeginDate.getText()[0:10]
        if (self.isValidDate(beginDate) and not beginDate.isspace() and not len(beginDate)==0):
            isBeginDate = "'"+beginDate+"'"

        endDate = self.txtEndDate.getText()[0:10]
        if (self.isValidDate(endDate) and not endDate.isspace() and not len(endDate)==0):
            isEndDate = "'"+endDate+"'"

        idTransac = self.txtTrancId.getText()
        if (not idTransac.isspace() and not len(idTransac)==0):
            isIdTransac = "'"+idTransac+"'"  

        clienteId = self.txtClient.getText()
        if (not clienteId.isspace() and not len(clienteId)==0):
            isClient = "'"+clienteId+"'"

        amount = self.txtMoney.getText()
        if (not amount.isspace() and not len(amount)==0):
            isAmount = "'"+amount+"'"
        
        if (not len(self.cmbCurrency.getSelection())==0):
            isCurrency = str(self.currencyIndices[self.cmbCurrency.getSelectionIndex()])
        
        idCust = self.txtCustId.getText()
        if (not idCust.isspace() and not len(idCust)==0):
            isIdCust = "'"+idCust+"'"

        if (not len(self.cmbPayment.getSelection())==0):
            isPayment = str(self.paymentIndices[self.cmbPayment.getSelectionIndex()])

        try:
            query = "EXEC [dbo].[sp_Events] "+isBeginDate+", "+isEndDate+", "+isIdTransac+", "+isCurrency+", "+isPayment+", "+isIdCust+", "+isClient
            df = self.ssConn.tableToDataFrame(query)
            self.tblTable.insertDataFrame(df)
        except Exception as e:
            Log.showError("No se puede generar este reporte")
            self.destroy()
            return
    
    def isValidDate(self, date:str):
        return Util.isValidDate(date)

            

