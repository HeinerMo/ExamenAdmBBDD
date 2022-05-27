from gui.components.Window import Window
from util.SSConection import PySSAdmin
import util.Log as Log

class RemovePermissionWindow (Window):
    def __init__(self, ssConn:PySSAdmin):
        Window.__init__(self)
        self.ssConn = ssConn
        self.onTop()
        self.initComponents()

    def initComponents(self):
        lblName = self.createLabel()
        lblName.setText("Nombre de Usuario")
        lblName.setBackgroundColor("white")
        lblName.grid(0,0,5,95)

        self.txtName = self.createTextField()
        self.txtName.setSize(100, 50)
        self.txtName.grid(1,0,5,5)

        lblTabla = self.createLabel()
        lblTabla.setText("Tabla")
        lblTabla.setBackgroundColor("white")
        lblTabla.grid(2,0,5,5)

        self.cmbTable = self.createComboBox()
        self.cmbTable.setSize(20, 50)
        self.cmbTable.grid(3,0,5,5)
        self.cmbTable.setValues(["CUSTOMER_ACCOUNTS", "TRANSACTIONS", "USERS"])

        lblPermission = self.createLabel()
        lblPermission.setText("Permiso")
        lblPermission.setBackgroundColor("white")
        lblPermission.grid(4,0,5,5)

        self.cmbPermission = self.createComboBox()
        self.cmbPermission.setSize(20, 50)
        self.cmbPermission.grid(5,0,5,5)
        self.cmbPermission.setValues(["Agregar Usuarios", "Lectura"])

        btnLogin = self.createButton()
        btnLogin.setText("Agregar")
        btnLogin.setBackgroundColor("#004972")
        btnLogin.setForegroundColor("white")
        btnLogin.grid(6,0,5,5)
        btnLogin.setSize(15, 5)
        btnLogin.execMethod(self.onRemoveAction)
    
    def onRemoveAction(self):
        user = "Holaa"
        password = "Holaa"
        query = "EXEC [dbo].[sp_AddUserX]  N'Pruebaaaaaa', N'Bb123'"
        state = self.ssConn.execQuery(query)
        if (state != 1):
            Log.showError(state)
            state.close()
        else:
            Log.showInfo("Usuario Registrado")





