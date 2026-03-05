from controlador.ctrl_Acerca import controladorAcerca
from controlador.ctrl_Reservas import Controlador_Reservas_Usuarios
from vista.VentanaPrincipal import Ui_MainWindow


from PyQt6 import QtWidgets


class controladorMainUsuarios(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.vista = Ui_MainWindow()
        self.vista.setupUi(self)

        self.controlador_informacion = controladorAcerca()
        self.controlador_reservas = Controlador_Reservas_Usuarios()
        self.vista.menuAdministrador.menuAction().setVisible(False)


    # Conexion de las onpciones
        self.vista.actionReservervar.triggered.connect(self.ventana_reservas)
        self.vista.actionSalir.triggered.connect(self.salir)
        self.vista.actionAcerca_de.triggered.connect(self.mostrar_vent_acecade)

    def mostrar_vent_acecade(self):
        self.controlador_informacion.show()

    def ventana_reservas(self):
        self.controlador_reservas.show()


    def salir(self):
        self.close()
