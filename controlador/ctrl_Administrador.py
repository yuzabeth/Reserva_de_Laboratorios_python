from vista.Agendar import Ui_Agendar
from PyQt6 import QtWidgets


class controladorReservasAdministrador(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.vista = Ui_Agendar()
        self.vista.setupUi(self)

        self.vista.btnSalirRerservar.clicked.connect(self.salir)

    def salir(self):
        self.close()
