from vista.Acerca import Ui_Acerca
from PyQt6 import QtWidgets
class controladorAcerca(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.vista = Ui_Acerca()
        self.vista.setupUi(self)

        self.vista.btnSalirAcerca.clicked.connect(self.salir)

    def salir(self):

        self.close()
