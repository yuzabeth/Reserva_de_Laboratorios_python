import os
import pickle
from modelo.modLaboratorios import Laboratorios


class Archivos:
    def __init__(self):
        pass

    def GuardarArchivo(self, nombreArchivo, lista):
        with open(nombreArchivo, "wb") as f:
            pickle.dump(lista, f)

    def AbrirArchivo(self, nombreArchivo):
        try:
            with open(nombreArchivo, "rb") as l:
                lista = pickle.load(l)
            return lista
        except FileNotFoundError:
            print("No se ingresaron laboratorios.")

    def ExisteArchivo(self, nombreArchivo):
        if os.path.isfile(nombreArchivo) == True:  # El archivo existe
            return True
        else:  # el archivo no existe
            return False

    def BuscarUsuariosLogin(self, nombre_archivo, usuario, contrasenia):
        lista = self.AbrirArchivo(nombre_archivo)
        for i in lista:
            if i.correo == usuario and i.contrasenia == contrasenia:
                return True
        return False

    def BuscarUsuarioCedula(self, nombre_archivo, cedula):
        lista = self.AbrirArchivo(nombre_archivo)
        for i in lista:
            if i.cedula == cedula:
                return True
        return False

    def BuscarIndice(self, nombre_archivo, atributo):
        lista = self.AbrirArchivo(nombre_archivo)
        return next((indice for indice, elemento in enumerate(lista) if elemento.cedula == atributo), False)

    def ObtenerPersona(self, nombre_archivo, cedula):
        lista = self.AbrirArchivo(nombre_archivo)
        for i in lista:
            if i.cedula == cedula:
                listaauxiliar = [i.cedula, i.nombre, i.apellido, i.telefono, i.rol, i.correo, i.contrasenia]
                                   #cedula, nombre, apellido, telefono, rol, correo, contrasenia
                return listaauxiliar
        return False

#OPERACIONES PARA EL CRUD DE USUARIOS
    def cambiar_datos(self, cedula, nombre, apellido, telefono, rol, correo, contrasenia):
        lista = self.AbrirArchivo('usuarios.dat')
        for usuario in lista:
            if usuario.cedula == cedula:
                usuario.nombre = nombre
                usuario.apellido = apellido
                usuario.telefono = telefono
                usuario.rol = rol
                usuario.correo = correo
                usuario.contrasenia = contrasenia

        self.GuardarArchivo('usuarios.dat', lista)

    def eliminar_usuario(self, nombre_archivo, cedula):
        lista = self.AbrirArchivo(nombre_archivo)

        for usuario in lista:
            if usuario.cedula == cedula:
                lista.remove(usuario)
                break

        self.GuardarArchivo(nombre_archivo, lista)

    #OPERACIONES PARA EL CRUD DE LABORATORIOS
    def get_laboratorio(self, nombre_archivo, nombreLaboratorio):
        lista = self.AbrirArchivo(nombre_archivo)
        for i in lista:
            if isinstance(i, Laboratorios) and i.nombreLaboratorio == nombreLaboratorio:
                listaauxiliar = [i.nombreLaboratorio, i.encargado, i.ubicacion, i.maquinas]
                return listaauxiliar
        return False

    def buscar_indice_laboratorio(self, nombre_archivo, nombreLaboratorio):
        lista = self.AbrirArchivo(nombre_archivo)
        indice = next((indice for indice, elemento in enumerate(lista) if elemento.nombreLaboratorio == nombreLaboratorio), -1)
        return indice

    def cambiar_datos_laboratorio(self, nombreLaboratorio,encargado, ubicacion, maquinas):
        lista = self.AbrirArchivo('laboratorios.dat')
        for laboratorio in lista:
            if laboratorio.nombreLaboratorio == nombreLaboratorio:
                laboratorio.encargado = encargado
                laboratorio.ubicacion = ubicacion
                laboratorio.maquinas = maquinas

        self.GuardarArchivo('laboratorios.dat', lista)

    def eliminar_laboratorio(self, nombre_archivo, nombreLaboratorio):
        lista = self.AbrirArchivo(nombre_archivo)

        for laboratorio in lista:
            if isinstance(laboratorio, Laboratorios) and laboratorio.nombreLaboratorio == nombreLaboratorio:
                lista.remove(laboratorio)
                break

        self.GuardarArchivo(nombre_archivo, lista)