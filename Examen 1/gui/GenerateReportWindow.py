from gui.ReportCustomersWindow import ReportCustomersWindow
from gui.ReportUsers import ReportUsers
from gui.components.Window import Window
from util.SSConection import PySSAdmin
import util.Log as Log

class GenerateReportWindow (Window):
    def __init__(self, ssConn:PySSAdmin):
        Window.__init__(self)
        self.ssConn = ssConn
        self.initComponents()

    def initComponents(self):
        btnLogin = self.createButton()
        btnLogin.setText("CUSTOMER_ACCOUNTS")
        btnLogin.setBackgroundColor("#004972")
        btnLogin.setForegroundColor("white")
        btnLogin.grid(0,0,5,5)
        btnLogin.setSize(20, 5)
        btnLogin.execMethod(self.onGenCustomerAction)

        btnLogin = self.createButton()
        btnLogin.setText("TRANSACTIONS")
        btnLogin.setBackgroundColor("#004972")
        btnLogin.setForegroundColor("white")
        btnLogin.grid(0,1,5,5)
        btnLogin.setSize(20, 5)
        btnLogin.execMethod(self.onGenTransactionAction)

        btnLogin = self.createButton()
        btnLogin.setText("USERS")
        btnLogin.setBackgroundColor("#004972")
        btnLogin.setForegroundColor("white")
        btnLogin.grid(1,0,5,5)
        btnLogin.setSize(20, 5)
        btnLogin.execMethod(self.onGenUserAction)
        
    def onGenCustomerAction(self):
        reportCust = ReportCustomersWindow(self.ssConn)
        reportCust.setSize(500, 500)
        reportCust.setTitle("Reporte de CUSTOMER_ACCOUNTS")
        reportCust.setLocationCenter()

    def onGenTransactionAction(self):
        pass

    def onGenUserAction(self):
        reportCust = ReportUsers(self.ssConn)
        reportCust.setSize(500, 500)
        reportCust.setTitle("Reporte de USERS")
        reportCust.setLocationCenter()

    

