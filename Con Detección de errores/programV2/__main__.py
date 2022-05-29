#pip install tk
#pip install pyodbc
from gui.LoginWindow import LoginWindow

def main():

    lw = LoginWindow()
    lw.setSize(800, 600)
    lw.setLocationCenter()
    lw.setTitle("Iniciar Sesión")
    lw.startWin()

if __name__ == '__main__':
    main()