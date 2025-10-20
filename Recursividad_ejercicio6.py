# Algoritmo para contar las vocales de una cadena usando recursividad
# Diego Emiliano Moran Trejo

class ContarVocales:
    def __init__(self, cadena):
        self.cadena = cadena  

    def calcular(self, cadena):
        if cadena == "":  
            return 0
        else:
            if cadena[0].lower() in 'aeiou':  
                return 1 + self.calcular(cadena[1:])  
            else:
                return self.calcular(cadena[1:])  

    def imprimir(self):
        print(self.calcular(self.cadena))  

objVocales = ContarVocales("Recursividad")
objVocales.imprimir()  
print("Diego Emiliano Moran Trejo")
