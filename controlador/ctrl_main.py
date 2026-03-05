from controlador.ctrl_Acerca import controladorAcerca
from controlador.ctrl_Administrador import controladorReservasAdministrador
from controlador.ctrl_Laboratorio import controladorLaboratorio
from controlador.ctrl_Usuarios import ControladorUsuarios
from controlador.ctrl_Reportes import controladorReportes
from vista.VentanaPrincipal import Ui_MainWindow


from PyQt6 import QtWidgets


class controladorMainAdministrador(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.vista = Ui_MainWindow()
        self.vista.setupUi(self)

        self.controlador_usuarios = ControladorUsuarios()
        self.controlador_informacion = controladorAcerca()
        self.controlador_laboratorios = controladorLaboratorio()
        self.controlador_reservas = controladorReservasAdministrador()
        self.controlador_reportes = controladorReportes()
        # Conexion de las onpciones
        self.vista.actionUsuarios.triggered.connect(self.ventana_usuarios)
        self.vista.actionLaboratorios.triggered.connect(self.ventana_laboratorios)
        self.vista.actionReservervar.triggered.connect(self.ventana_reservas)
        self.vista.actionAcerca_de.triggered.connect(self.mostrar_vent_acecade)
        self.vista.actionSalir.triggered.connect(self.salir)
        self.vista.actionReportes.triggered.connect(self.ventana_reportes)


    def ventana_usuarios(self):
        self.controlador_usuarios.show()

    def ventana_laboratorios(self):
        self.controlador_laboratorios.show()

    def mostrar_vent_acecade(self):
        self.controlador_informacion.show()

    def ventana_reservas(self):
        self.controlador_reservas.show()

    def ventana_reportes(self):
        self.controlador_reportes.show()

    def salir(self):
        self.close()
