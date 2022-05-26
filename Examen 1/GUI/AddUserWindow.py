from Window import Window
from SSConection import PySSAdmin
import Log

class AddUserWindow (Window):
    def __init__(self, ssConn:PySSAdmin):
        Window.__init__(self)
        self.ssConn = ssConn
        self.onTop()
        self.initComponents()

    def initComponents(self):
        btnLogin = self.createButton()
        btnLogin.setText("Agregar")
        btnLogin.setBackgroundColor("#004972")
        btnLogin.setForegroundColor("white")
        btnLogin.setPosition(0, 200)
        btnLogin.setSize(15, 5)
        btnLogin.execMethod(self.onLoginAction)

        lblName = self.createLabel()
        lblName.setText("Nombre de Usuario")
        lblName.setBackgroundColor("white")
        lblName.setPosition(0, 0)

        self.txtName = self.createTextField()
        self.txtName.setSize(100, 50)
        self.txtName.setPosition(0, 50)

        lblPassword = self.createLabel()
        lblPassword.setText("Contraseña")
        lblPassword.setBackgroundColor("white")
        lblPassword.setPosition(0, 100)

        self.txtPassword = self.createTextField()
        self.txtPassword.setSize(100, 50)
        self.txtPassword.setPosition(0, 150)
    
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





