from vista.Usuarios import Ui_Usuarios
from modelo.modUsuarios import Usuario
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem
from modelo.Archivos import Archivos
from modelo.Validaciones import Validaciones


class ControladorUsuarios(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.vista = Ui_Usuarios()
        self.vista.setupUi(self)

        # Pagina de registro
        self.vista.btnNuevoUsuario.clicked.connect(self.agregar_usuario)
        self.vista.btnSalirUsuario.clicked.connect(self.salir)
        self.vista.btnBuscarUsuario.clicked.connect(self.buscarUsuarios)
        self.vista.btnModificarUsuario.clicked.connect(self.modificarUsuarios)
        self.vista.btnEliminarUsuario.clicked.connect(self.eliminarUsuario)
        self.vista.btnListarUsuario.clicked.connect(self.listarUsuarios)

    def salir(self):
        self.close()


    def agregar_usuario(self):
        validaciones = Validaciones()
        archivos = Archivos()
        lista_usuarios = []
        cedula = self.vista.txtCedulaUsuario.text()
        nombre = self.vista.txtNombreUsuario.text()
        apellido = self.vista.txtApellidoUsuario.text()
        telefono = self.vista.txtTelefonoUsuario.text()
        correo = self.vista.txtCorreoUsuario.text()
        contrasenia = self.vista.txtDireccionUsuario.text()
        rol = self.vista.comboBoxDocEst.currentText()
        texto = [cedula, nombre, apellido, telefono, correo, contrasenia]
        if rol != 'Seleccione una opción:':
            if validaciones.ingresa_texto(texto):
                if len(cedula) == 10 and validaciones.validar_cedula(cedula):
                    if validaciones.valida_entero(telefono):
                        if archivos.ExisteArchivo('usuarios.dat'):
                            if not archivos.ObtenerPersona('usuarios.dat', cedula):
                                lista_usuarios = archivos.AbrirArchivo('usuarios.dat')
                                crear_usuario = Usuario(cedula, nombre, apellido, telefono, rol, correo, contrasenia)
                                lista_usuarios.append(crear_usuario)
                                archivos.GuardarArchivo('usuarios.dat', lista_usuarios)
                                QMessageBox.information(self, "Usuarios", "Usuario agregado correctamente.")
                            else:
                                QMessageBox.information(self, "Usuarios", "El usuario ya existe")
                        if not archivos.ExisteArchivo('usuarios.dat'):
                            crear_usuario = Usuario(cedula, nombre, apellido, telefono, rol, correo, contrasenia)
                            lista_usuarios.append(crear_usuario)
                            archivos.GuardarArchivo('usuarios.dat', lista_usuarios)
                            QMessageBox.information(self, "Usuarios", "Usuario agregado correctamente.")
                    else:
                        QMessageBox.warning(self, "Error", "El teléfono es icorrecto.")
                else:
                    QMessageBox.warning(self, "Error", "Cédula incorrecta")
            else:
                QMessageBox.warning(self, "Error", "Existen espacios vacíos.")
        else:
            QMessageBox.warning(self, "Error", "Seleccione un rol.")

    def buscarUsuarios(self):
        try:
            archivos = Archivos()
            cedula = self.vista.txtCedulaUsuario.text()

            if archivos.BuscarUsuarioCedula('usuarios.dat', cedula):
                # Si la persona con la cédula especificada existe
                info_usuario = archivos.ObtenerPersona('usuarios.dat', cedula)
                # Actualizar los campos de texto en la interfaz con la información del usuario
                self.vista.txtNombreUsuario.setText(info_usuario[1])
                self.vista.txtApellidoUsuario.setText(info_usuario[2])
                self.vista.txtTelefonoUsuario.setText(info_usuario[3])
                self.vista.txtCorreoUsuario.setText(info_usuario[4])
                self.vista.comboBoxDocEst.setCurrentText(info_usuario[5])
                self.vista.txtDireccionUsuario.setText(info_usuario[6])

                QMessageBox.information(self, "Usuarios", "Usuario encontrado.")
                # Aquí puedes agregar lógica adicional según tus necesidades
            else:
                # Si la persona con la cédula especificada no existe
                QMessageBox.warning(self, "Usuarios", "Usuario no encontrado.")
                # Aquí puedes agregar lógica adicional según tus necesidades

        except Exception as e:
            print(f"Error al buscar usuarios: {e}")
            QMessageBox.critical(self, "Error", f"Ocurrió un error al buscar usuarios: {e}")


    def modificarUsuarios(self):
        try:
            validaciones = Validaciones()
            archivos = Archivos()
            #lista_usuarios = []
            cedula = self.vista.txtCedulaUsuario.text()
            nombre = self.vista.txtNombreUsuario.text()
            apellido = self.vista.txtApellidoUsuario.text()
            telefono = self.vista.txtTelefonoUsuario.text()
            correo = self.vista.txtCorreoUsuario.text()
            contrasenia = self.vista.txtDireccionUsuario.text()
            rol = self.vista.comboBoxDocEst.currentText()
            texto = [cedula, nombre, apellido, telefono, correo, contrasenia]

            if rol != 'Seleccione una opción:':
                if validaciones.ingresa_texto(texto):
                    if len(cedula) == 10 and validaciones.validar_cedula(cedula):
                        if validaciones.valida_entero(telefono):
                            if archivos.BuscarUsuarioCedula('usuarios.dat', cedula):
                                # Si la persona con la cédula especificada existe
                                archivos.cambiar_datos(cedula, nombre, apellido, telefono, rol, correo, contrasenia)
                                QMessageBox.information(self, "Usuarios", "Usuario modificado correctamente.")
                                # Puedes agregar lógica adicional según tus necesidades
                            else:
                                # Si la persona con la cédula especificada no existe
                                QMessageBox.warning(self, "Usuarios", "Usuario no encontrado.")
                                # Puedes agregar lógica adicional según tus necesidades
                        else:
                            QMessageBox.warning(self, "Error", "El teléfono es incorrecto.")
                    else:
                        QMessageBox.warning(self, "Error", "Cédula incorrecta")
                else:
                    QMessageBox.warning(self, "Error", "Existen espacios vacíos.")
            else:
                QMessageBox.warning(self, "Error", "Seleccione un rol.")

        except Exception as e:
            print(f"Error al modificar usuarios: {e}")
            QMessageBox.critical(self, "Error", f"Ocurrió un error al modificar usuarios: {e}")

    def eliminarUsuario(self):
        try:
            archivos = Archivos()
            cedula = self.vista.txtCedulaUsuario.text()

            if archivos.BuscarUsuarioCedula('usuarios.dat', cedula):
                # Si la persona con la cédula especificada existe
                archivos.eliminar_usuario('usuarios.dat', cedula)
                QMessageBox.information(self, "Usuarios", "Usuario eliminado correctamente.")
                # Puedes agregar lógica adicional según tus necesidades
            else:
                # Si la persona con la cédula especificada no existe
                QMessageBox.warning(self, "Usuarios", "Usuario no encontrado.")
                # Puedes agregar lógica adicional según tus necesidades

        except Exception as e:
            print(f"Error al eliminar usuario: {e}")
            QMessageBox.critical(self, "Error", f"Ocurrió un error al eliminar usuario: {e}")


    def listarUsuarios(self):
        archivos = Archivos()
        lista = archivos.AbrirArchivo('usuarios.dat')
        # Definimos los títulos de las columanas
        cabecera = ["Cédula", "Nombre", "Apellido", "Teléfono", "Rol", "Correo"]
        self.vista.tabUsuarios.setColumnCount(len(cabecera))
        self.vista.tabUsuarios.setHorizontalHeaderLabels(cabecera)
        self.vista.tabUsuarios.setRowCount(len(lista))
        # Establecer el formato de texto en negrita para los encabezados
        header_font = self.vista.tabUsuarios.horizontalHeader().font()
        header_font.setBold(True)
        self.vista.tabUsuarios.horizontalHeader().setFont(header_font)

        for row_idx, persona in enumerate(lista):
            self.vista.tabUsuarios.setItem(row_idx, 0, QTableWidgetItem(persona.cedula))
            self.vista.tabUsuarios.setItem(row_idx, 1, QTableWidgetItem(persona.nombre))
            self.vista.tabUsuarios.setItem(row_idx, 2, QTableWidgetItem(persona.apellido))
            self.vista.tabUsuarios.setItem(row_idx, 3, QTableWidgetItem(persona.telefono))
            self.vista.tabUsuarios.setItem(row_idx, 4, QTableWidgetItem(persona.rol))
            self.vista.tabUsuarios.setItem(row_idx, 5, QTableWidgetItem(persona.correo))


