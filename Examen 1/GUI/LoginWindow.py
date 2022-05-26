from Window import Window
from SSConection import PySSAdmin
from UserWindow import UserWindow
import Log

class LoginWindow (Window):
    def __init__(self):
        Window.__init__(self)
        self.initComponents()

    def initComponents(self):
        btnLogin = self.createButton()
        btnLogin.setText("Iniciar Sesión")
        btnLogin.setBackgroundColor("#004972")
        btnLogin.setForegroundColor("white")
        btnLogin.setPosition(400, 500)
        btnLogin.setSize(15, 5)
        btnLogin.execMethod(self.onLoginAction)

        lblSubTitle = self.createLabel()
        lblSubTitle.setText("IF5000_Examen1_C07409_B85042_B87581")
        lblSubTitle.setBackgroundColor("white")
        lblSubTitle.setPosition(200, 200)

        lblName = self.createLabel()
        lblName.setText("Nombre de Usuario")
        lblName.setBackgroundColor("white")
        lblName.setPosition(400, 250)

        self.txtName = self.createTextField()
        self.txtName.setSize(100, 50)
        self.txtName.setPosition(400, 300)

        lblPassword = self.createLabel()
        lblPassword.setText("Contraseña")
        lblPassword.setBackgroundColor("white")
        lblPassword.setPosition(400, 350)

        self.txtPassword = self.createTextField()
        self.txtPassword.setSize(100, 50)
        self.txtPassword.setPosition(400, 400)
        self.txtPassword.maskText("*")
    
    def onLoginAction(self):
        ssConn = PySSAdmin()
        #state = ssConn.connectToDB("TONI-WIN11", "AdventureWorks2019", self.txtName.getText(), self.txtPassword.getText())
        state = ssConn.connectToDB("TONI-WIN11", "AdventureWorks2019", "superadmin", "123Password")
        if (state != 1):
            Log.showError(state)
        else:
            #TODO CHECK IF THE USER HAVE PERMISSIONS TO CREATE NEW USERS OR GENERATE REPORTS
            uw = UserWindow(ssConn)        
            uw.setSize(800, 600)
            uw.setLocationCenter()
            uw.setTitle("Modificar Usuarios")
            self.destroy()
            uw.startWin()
            

