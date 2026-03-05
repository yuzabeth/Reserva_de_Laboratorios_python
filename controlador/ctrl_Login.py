from vista.Login import Ui_Login
from controlador.ctrl_main import controladorMainAdministrador
from controlador.ctrl_principal_Usuarios import controladorMainUsuarios
from PyQt6 import QtWidgets


class controladorLogin(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.vista = Ui_Login()
        self.vista.setupUi(self)

        self.controlador_principal_admin = controladorMainAdministrador()
        self.controlador_principal_user = controladorMainUsuarios()
        self.vista.btnIngresarLogin.clicked.connect(self.mostrar_vent_principal)

    '''
    def keyPressEvent(self, event):
        # Manejar el evento de tecla presionada
        if event.key() in {QtCore.Qt.Key_Enter, QtCore.Qt.Key_Return}:
            self.mostrar_vent_principal()'''

    def mostrar_vent_principal(self):
        user = self.vista.txtCorreoLogin.text()
        password = self.vista.txtContrasenaLogin.text()
        if user == 'admin' and password == 'admin':
            self.controlador_principal_admin.show()
        else:
            self.controlador_principal_user.show()
