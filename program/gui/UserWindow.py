from gui.AddUserWindow import AddUserWindow
from gui.AddPermissionWindow import AddPermissionWindow
from gui.RemovePermissionWindow import RemovePermissionWindow
from gui.GenerateReportWindow import GenerateReportWindow
from gui.components.Window import Window
from util.SSConection import PySSAdmin
import util.Log as Log

class UserWindow (Window):
    def __init__(self, ssConn:PySSAdmin):
        Window.__init__(self)
        self.ssConn = ssConn
        self.initComponents()

    def initComponents(self):

        btnAddUser = self.createButton()
        btnAddUser.setText("Añadir Usuario")
        btnAddUser.setBackgroundColor("#004972")
        btnAddUser.setForegroundColor("white")
        btnAddUser.grid(0,0,5,5)
        btnAddUser.setSize(20,5)
        btnAddUser.execMethod(self.onAddUserAction)

        btnAddPermission = self.createButton()
        btnAddPermission.setText("Añadir Permisos")
        btnAddPermission.setBackgroundColor("#004972")
        btnAddPermission.setForegroundColor("white")
        btnAddPermission.grid(0,1,5,5)
        btnAddPermission.setSize(20,5)
        btnAddPermission.execMethod(self.onAddPermissionAction)

        btnRemovePermission = self.createButton()
        btnRemovePermission.setText("Eliminar permisos")
        btnRemovePermission.setBackgroundColor("#004972")
        btnRemovePermission.setForegroundColor("white")
        btnRemovePermission.grid(1,0,5,5)
        btnRemovePermission.setSize(20,5)
        btnRemovePermission.execMethod(self.onRemovePermissionAction)

        btnGenReport = self.createButton()
        btnGenReport.setText("Generar Reporte")
        btnGenReport.setBackgroundColor("#004972")
        btnGenReport.setForegroundColor("white")
        btnGenReport.grid(1,1,5,5)
        btnGenReport.setSize(20,5)
        btnGenReport.execMethod(self.onGenerateReportAction)
    
    def onAddUserAction(self):
        addUser = AddUserWindow(self.ssConn)
        addUser.setSize(300, 230)
        addUser.setTitle("Agregar Usuario")
        addUser.setLocation(self.getPosX()+400, self.getPosY()+100)

    def onAddPermissionAction(self):
        addPermission = AddPermissionWindow(self.ssConn)
        addPermission.setSize(300, 300)
        addPermission.setTitle("Agregar Permisos")
        addPermission.setLocation(self.getPosX()+400, self.getPosY()+100)

    def onRemovePermissionAction(self):
        removePermission = RemovePermissionWindow(self.ssConn)
        removePermission.setSize(300, 300)
        removePermission.setTitle("Eliminar Permisos")
        removePermission.setLocation(self.getPosX()+400, self.getPosY()+100)

    def onGenerateReportAction(self):
        genReport = GenerateReportWindow(self.ssConn)
        genReport.setSize(320, 190)
        genReport.setTitle("Generar Reporte")
        genReport.setLocation(self.getPosX()+400, self.getPosY()+100)