from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox
from modelo.Archivos import Archivos
from modelo.Validaciones import Validaciones
from vista.Agendar import Ui_Agendar
from PyQt6 import QtWidgets


class Controlador_Reservas_Usuarios(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.vista = Ui_Agendar()
        self.vista.setupUi(self)

        self.vista.btnBuscarReservar.clicked.connect(self.buscarReserva)
        self.vista.btnNuevoReservar.clicked.connect(self.agendarReserva)
        self.vista.btnModificarReservar.clicked.connect(self.modificarReserva)
        self.vista.btnEliminarReservar.clicked.connect(self.eliminarReserva)
        self.vista.btnListarReservar.clicked.connect(self.listarReserva)
        self.vista.btnSalirRerservar.clicked.connect(self.salir)

    def salir(self):
        self.close()

    # cedula,nombre,apellido,laboratorio,NroPersonas,fecha,hora
    def buscarReserva(self):
        validaciones = Validaciones()
        archivos = Archivos()
        listaReservas = []

        cedula = self.vista.txtCedulaReservar.text()
        nombre = self.vista.txtNombreReservar.text()
        apellido = self.vista.txtApellidoReservar.text()
        laboratorio = self.vista.comboBoxLabReservar.currentText()
        nroPersonas = self.vista.spinBoxReservar.currentText()
        fecha = self.vista.calendarWidget.selectedDate().toString(Qt.DateFormat.ISODate)
        hora = self.vista.timeEditHora.time().toString(Qt.DateFormat.ISODate)

        if len(cedula) == 10 and validaciones.validar_cedula(cedula):
            pass
        else:
            QMessageBox.warning(self, "Error", "Cédula incorrecta")

    def agendarReserva(self):
        pass

    def modificarReserva(self):
        pass

    def eliminarReserva(self):
        pass

    def listarReserva(self):
        pass
