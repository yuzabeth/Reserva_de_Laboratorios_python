class Validaciones:
    def __init__(self):
        pass

    def validar_cedula(self, cedula):
        par = cedula[::2]
        impar = cedula[1:8:2]
        return int(cedula[9]) == 10 - sum(list(map(lambda x: x*2-9 , filter(lambda x:x*2 >9 ,[int(par[i])for i in range(5)])))  + list(map(lambda x: x*2 , filter(lambda x:x*2 <9, [int(par[i])for i in range(5)])))  +  list([int(impar[i])for i in range(4)])) % 10

    def ingresa_texto(self, lista):
        for x in lista:
            if x == "":
                return False
        return True

    def texto_vacio(self, texto):
        if texto == "":
            return False
        return True

    def valida_entero(self, telefono):
        return telefono.isdigit()

    def valida_solo_letras(self,texto):
        for i in range(len(texto)):
            if texto[i].isdigit()==True:
                return False
        return True

