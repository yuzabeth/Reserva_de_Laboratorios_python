from controlador.ctrl_Login import controladorLogin
from PyQt6 import QtWidgets
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    controlador = controladorLogin()
    controlador.show()
    app.exec()
