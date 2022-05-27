from gui.AddUserWindow import AddUserWindow
from gui.AddPermissionWindow import AddPermissionWindow
from gui.RemovePermissionWindow import RemovePermissionWindow
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
        btnLogin.execMethod(self.onAddUserAction)

        btnLogin = self.createButton()
        btnLogin.setText("TRANSACTIONS")
        btnLogin.setBackgroundColor("#004972")
        btnLogin.setForegroundColor("white")
        btnLogin.grid(0,1,5,5)
        btnLogin.setSize(20, 5)
        btnLogin.execMethod(self.onAddPermissionAction)

        btnLogin = self.createButton()
        btnLogin.setText("USERS")
        btnLogin.setBackgroundColor("#004972")
        btnLogin.setForegroundColor("white")
        btnLogin.grid(1,0,5,5)
        btnLogin.setSize(20, 5)
        btnLogin.execMethod(self.onRemovePermissionAction)
    
    def onAddUserAction(self):
        addUser = AddUserWindow(self.ssConn)
        addUser.setSize(300, 300)
        addUser.setTitle("Agregar Usuario")
        addUser.setLocationCenter()

    def onAddPermissionAction(self):
        addPermission = AddPermissionWindow(self.ssConn)
        addPermission.setSize(300, 300)
        addPermission.setTitle("Agregar Permisos")
        addPermission.setLocationCenter()

    def onRemovePermissionAction(self):
        addPermission = RemovePermissionWindow(self.ssConn)
        addPermission.setSize(300, 300)
        addPermission.setTitle("Agregar Permisos")
        addPermission.setLocationCenter()

    

