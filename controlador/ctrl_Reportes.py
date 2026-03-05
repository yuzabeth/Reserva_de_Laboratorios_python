from vista.Reportes import Ui_Reportes
from PyQt6 import QtWidgets
class controladorReportes(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.vista = Ui_Reportes()
        self.vista.setupUi(self)

        self.vista.btnSalirReportes.clicked.connect(self.salir)

    def salir(self):

        self.close()
