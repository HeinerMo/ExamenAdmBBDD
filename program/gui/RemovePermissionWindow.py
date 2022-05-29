from gui.components.Window import Window
from util.SSConection import PySSAdmin
import util.Log as Log
import pyodbc

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
        try:
            user = "'"+self.txtName.getText()+"'"
            permission = -1
            table = "NULL"
            
            if (self.cmbPermission.getSelection() == "Lectura"):
                table = self.cmbTable.getSelection()
                if (table == "CUSTOMER_ACCOUNTS"):
                    table = "'"+"[CUSTOMERS].[tb_CUSTOMER_ACCOUNTS]"+"'"
                elif (table == "TRANSACTIONS"):
                    table = "'"+"[FINANCIAL_DEPOSIT].[tb_EVENTS]"+"'"
                elif (table == "USERS"):
                    table = "'"+"[CLI_COMMON].[tb_USERS]"+"'"
            
            if (self.cmbPermission.getSelection() == "Lectura"):
                permission = 2
            elif (self.cmbPermission.getSelection() == "Agregar Usuarios"):
                permission = 1

            query = "EXEC [dbo].[sp_RemovePermissions] "+user+", "+table+", "+str(permission)
            cursor = self.ssConn.getCursor().execute(query)
            cursor.commit()
        except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            print(sqlstate)
            if sqlstate == '08001':
                return ""

            print(ex.args[1])

        Log.showInfo("Permiso revocado")
        cursor.close()
        del cursor





