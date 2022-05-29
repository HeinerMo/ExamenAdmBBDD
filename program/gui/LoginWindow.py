from gui.components.Window import Window
from util.SSConection import PySSAdmin
from gui.UserWindow import UserWindow
import util.Log as Log

class LoginWindow (Window):
    def __init__(self):
        Window.__init__(self)
        self.initComponents()

    def initComponents(self):
        lblSubTitle = self.createLabel()
        lblSubTitle.setText("IF5000_Examen1_C07409_B85042_B87581")
        lblSubTitle.setBackgroundColor("white")
        lblSubTitle.grid(0,0,5,300)

        lblName = self.createLabel()
        lblName.setText("Nombre de Usuario")
        lblName.setBackgroundColor("white")
        lblName.grid(1,0,5,5)

        self.txtName = self.createTextField()
        self.txtName.setSize(100, 50)
        self.txtName.grid(2,0,5,5)

        lblPassword = self.createLabel()
        lblPassword.setText("Contraseña")
        lblPassword.setBackgroundColor("white")
        lblPassword.grid(3,0,5,5)

        self.txtPassword = self.createTextField()
        self.txtPassword.setSize(100, 50)
        self.txtPassword.grid(4,0,5,5)
        self.txtPassword.maskText("*")

        btnLogin = self.createButton()
        btnLogin.setText("Iniciar Sesión")
        btnLogin.setBackgroundColor("#004972")
        btnLogin.setForegroundColor("white")
        btnLogin.grid(5,0,5,5)
        btnLogin.setSize(15, 5)
        btnLogin.execMethod(self.onLoginAction)
    
    def onLoginAction(self):
        server = "TONI-WIN11"
        db = "TRANSACTION_PROCESSING_EXAMEN"
        ssConn = PySSAdmin()
        state = ssConn.connectToDB(server, db, self.txtName.getText(), self.txtPassword.getText())
        #state = ssConn.connectToDB(server, db, "", "")

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
            

