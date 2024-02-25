class Herramientas:

    def __init__(self,lista):
        self.lista_numeros = lista

    
    def listaPrimos (self):
        for i in self.lista_numeros:
            if self.esPrimo(i):
                print("El numero", i, "es primo")
            else:
                print("El numero", i, "no es primo")

    def esPrimo (self, numero):
        if numero < 2:
            return False
        if numero == 2:
            return True
        for i in range(2, numero):
            if numero % i == 0:
                return False
        return True


    def numerosMasRepetidos (self):

        if len(self.lista_numeros) == 0:
            return None

        contador = {}

        for i in self.lista_numeros:
            if i in contador:
                contador[i] += 1
            else:
                contador[i] = 1

        maximo = max(contador, key=contador.get)
        repeticiones_max = contador[maximo]

        return maximo, repeticiones_max
    

    def convertidor_de_grados_lista (self,unidad_origen, unidad_destino):
        lista_convertida = []
        for i in self.lista_numeros:
            lista_convertida.append(self.convertidor_de_grados(i,unidad_origen,unidad_destino))
        return lista_convertida

    def convertidor_de_grados (self,valor, unidad_origen, unidad_destino):
        # C = (F - 32) * 5/9
        # F = (C * 9/5) + 32
        # K = C + 273.15
        # C = K - 273.15
        # F = K * 9/5 - 459.67
        # K = (F + 459.67) * 5/9
        if unidad_origen == "C" and unidad_destino == "F":
            return (valor * 9/5) + 32
        elif unidad_origen == "C" and unidad_destino == "K":
            return valor + 273.15
        elif unidad_origen == "F" and unidad_destino == "C":
            return (valor - 32) * 5/9
        elif unidad_origen == "F" and unidad_destino == "K":
            return (valor + 459.67) * 5/9
        elif unidad_origen == "K" and unidad_destino == "C":
            return valor - 273.15
        elif unidad_origen == "K" and unidad_destino == "F":
            return valor * 9/5 - 459.67
        else:
            return valor
        

    def factorial_lista (self):
        lista_factoriales = []
        for i in self.lista_numeros:
            lista_factoriales.append(self.factorial(i))
        return lista_factoriales
        
    def factorial (self,numero):
        if numero < 0:
            return None
        if type(numero) != int:
            return None
        if numero == 0:
            return "El factorial de 0 es 1"
        for i in range(1, numero):
            numero *= i

        return numero