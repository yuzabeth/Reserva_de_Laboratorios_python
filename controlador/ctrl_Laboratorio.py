from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem

from modelo.modLaboratorios import Laboratorios
from vista.Laboratorios import Ui_Laboratorios
from PyQt6 import QtWidgets
from modelo.Archivos import Archivos
from modelo.Validaciones import Validaciones

class controladorLaboratorio(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.vista = Ui_Laboratorios()
        self.vista.setupUi(self)

        # Ventana ingreso de laboratorios
        self.vista.btnNuevoLaboratorio.clicked.connect(self.agregar_laboratorio)
        self.vista.btnModificarLaboratorio.clicked.connect(self.modificar_laboratorio)
        self.vista.btnEliminarLaboratorio.clicked.connect(self.eliminar_laboratorio)
        self.vista.btnBuscarLaboratorio.clicked.connect(self.buscar_laboratorio)
        self.vista.btnListarLaboratorio.clicked.connect(self.listarLaboratorios)
        self.vista.btnSalirLaboratorios.clicked.connect(self.salir)

    def salir(self):
        self.close()

    def agregar_laboratorio(self):
        validaciones = Validaciones()
        archivos = Archivos()
        listaLaboratorio = []

        nombreLaboratorio = self.vista.txtNombreLaboratorio.text()
        encargado = self.vista.txtApellidoLaboratorio.text()
        ubicacion = self.vista.txtDireccionLaboratorio.text()
        maquinas = self.vista.txtTelefonoLaboratorio.text()

        texto = [nombreLaboratorio, encargado,ubicacion]
        if validaciones.ingresa_texto(texto):
            if maquinas != 0:
                if archivos.ExisteArchivo('laboratorios.dat'):
                    if archivos.get_laboratorio('laboratorios.dat', nombreLaboratorio):
                        QMessageBox.warning(self, "Error", "El laboratorio ya existe.")
                    else:
                        listaLaboratorio = archivos.AbrirArchivo('laboratorios.dat')
                        laboratorio = Laboratorios(nombreLaboratorio, encargado,ubicacion,maquinas)
                        listaLaboratorio.append(laboratorio)
                        archivos.GuardarArchivo('laboratorios.dat', listaLaboratorio)
                        QMessageBox.information(self, "Laboratorios", "Laboratorio agregado exitosamente.")
                else:
                    laboratorio = Laboratorios(nombreLaboratorio, encargado,ubicacion,maquinas)
                    listaLaboratorio.append(laboratorio)
                    archivos.GuardarArchivo('laboratorios.dat', listaLaboratorio)
                    QMessageBox.information(self, "Laboratorios", "Laboratorio agregado exitosamente.")
            else:
                QMessageBox.warning(self, "Error", "Error en la capacidad.")
        else:
            QMessageBox.warning(self, "Error", "Existen datos vacíos.")


    def buscar_laboratorio(self):
        archivos = Archivos()
        nombreLaboratorio = self.vista.txtNombreLaboratorio.text()

        if archivos.ExisteArchivo('laboratorios.dat'):
            datos_laboratorio = archivos.get_laboratorio('laboratorios.dat', nombreLaboratorio)
            if datos_laboratorio:
                # Muestra los datos en la interfaz, por ejemplo:
                self.vista.txtApellidoLaboratorio.setText(datos_laboratorio[1])
                self.vista.txtDireccionLaboratorio.setText(datos_laboratorio[2])
                self.vista.txtTelefonoLaboratorio.setText(datos_laboratorio[3])
            else:
                QMessageBox.information(self, "Laboratorios", "No se encontró el laboratorio.")
        else:
            QMessageBox.information(self, "Laboratorios", "No hay laboratorios registrados.")


    def modificar_laboratorio(self):
        archivos = Archivos()
        nombreLaboratorio = self.vista.txtNombreLaboratorio.text()
        encargado = self.vista.txtApellidoLaboratorio.text()
        ubicacion = self.vista.txtDireccionLaboratorio.text()
        maquinas = self.vista.txtTelefonoLaboratorio.text()

        if archivos.ExisteArchivo('laboratorios.dat'):
            if archivos.get_laboratorio('laboratorios.dat', nombreLaboratorio):
                archivos.cambiar_datos_laboratorio(nombreLaboratorio, encargado,ubicacion, maquinas)
                QMessageBox.information(self, 'Laboratorios', "Laboratorio actualizado exitosamente.")
            else:
                QMessageBox.information(self, 'Laboratorios', "No se encontró el laboratorio.")
        else:
            QMessageBox.information(self, 'Laboratorios', "No hay laboratorios registrados.")


    def eliminar_laboratorio(self):
        archivos = Archivos()
        nombreLaboratorio = self.vista.txtNombreLaboratorio.text()

        if archivos.ExisteArchivo('laboratorios.dat'):
            if archivos.get_laboratorio('laboratorios.dat', nombreLaboratorio):
                archivos.eliminar_laboratorio('laboratorios.dat', nombreLaboratorio)
                QMessageBox.information(self, "Laboratorios", "Laboratorio eliminado.")
            else:
                QMessageBox.information(self, "Laboratorios", "No se encontró el laboratorio.")
        else:
            QMessageBox.information(self, "Laboratorios", "No hay laboratorios registrados.")


    def listarLaboratorios(self):
        archivos = Archivos()
        lista_laboratorios = archivos.AbrirArchivo('laboratorios.dat')
        # Definimos los títulos de las columanas
        cabecera = ["Nombre", "Encargado", "Ubicacion", "Nro.Maquinas"]
        self.vista.tabLaboratorio.setColumnCount(len(cabecera))
        self.vista.tabLaboratorio.setHorizontalHeaderLabels(cabecera)
        self.vista.tabLaboratorio.setRowCount(len(lista_laboratorios))
        # Establecer el formato de texto en negrita para los encabezados
        header_font = self.vista.tabLaboratorio.horizontalHeader().font()
        header_font.setBold(True)
        self.vista.tabLaboratorio.horizontalHeader().setFont(header_font)

        for row_idx, laboratorio in enumerate(lista_laboratorios):
            self.vista.tabLaboratorio.setItem(row_idx, 0, QTableWidgetItem(laboratorio.nombreLaboratorio))
            self.vista.tabLaboratorio.setItem(row_idx, 1, QTableWidgetItem(laboratorio.encargado))
            self.vista.tabLaboratorio.setItem(row_idx, 2, QTableWidgetItem(laboratorio.ubicacion))
            self.vista.tabLaboratorio.setItem(row_idx, 3, QTableWidgetItem(laboratorio.maquinas))