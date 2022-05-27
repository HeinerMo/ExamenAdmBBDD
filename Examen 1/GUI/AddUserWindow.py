from gui.components.Window import Window
from util.SSConection import PySSAdmin
import util.Log as Log

class AddUserWindow (Window):
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

        lblPassword = self.createLabel()
        lblPassword.setText("Contraseña")
        lblPassword.setBackgroundColor("white")
        lblPassword.grid(2,0,5,5)

        self.txtPassword = self.createTextField()
        self.txtPassword.setSize(100, 50)
        self.txtPassword.grid(3,0,5,5)

        btnLogin = self.createButton()
        btnLogin.setText("Agregar")
        btnLogin.setBackgroundColor("#004972")
        btnLogin.setForegroundColor("white")
        btnLogin.grid(4,0,5,5)
        btnLogin.setSize(15, 5)
        btnLogin.execMethod(self.onLoginAction)
    
    def onLoginAction(self):
        user = "Holaa"
        password = "Holaa"
        query = "EXEC [dbo].[sp_AddUserX]  N'Pruebaaaaaa', N'Bb123'"
        state = self.ssConn.execQuery(query)
        if (state != 1):
            Log.showError(state)
            state.close()
        else:
            Log.showInfo("Usuario Registrado")





