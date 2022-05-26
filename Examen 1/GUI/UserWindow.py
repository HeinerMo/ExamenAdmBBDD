from AddUserWindow import AddUserWindow
from Window import Window
from SSConection import PySSAdmin
import Log

class UserWindow (Window):
    def __init__(self, ssConn:PySSAdmin):
        Window.__init__(self)
        self.ssConn = ssConn
        self.initComponents()

    def initComponents(self):
        btnLogin = self.createButton()
        btnLogin.setText("Añadir Usuario")
        btnLogin.setBackgroundColor("#004972")
        btnLogin.setForegroundColor("white")
        btnLogin.setPosition(0, 000)
        btnLogin.setSize(15, 5)
        btnLogin.execMethod(self.onLoginAction)

        btnLogin = self.createButton()
        btnLogin.setText("Añadir Permisos")
        btnLogin.setBackgroundColor("#004972")
        btnLogin.setForegroundColor("white")
        btnLogin.setPosition(0, 200)
        btnLogin.setSize(15, 5)
        btnLogin.execMethod(self.onLoginAction)

        btnLogin = self.createButton()
        btnLogin.setText("Eliminar Usuarios")
        btnLogin.setBackgroundColor("#004972")
        btnLogin.setForegroundColor("white")
        btnLogin.setPosition(0, 500)
        btnLogin.setSize(15, 5)
        btnLogin.execMethod(self.onLoginAction)
    
    def onLoginAction(self):
        addUser = AddUserWindow(self.ssConn)
        addUser.setSize(300, 300)
        addUser.setTitle("Agregar Usuario")
        addUser.setLocationCenter()

