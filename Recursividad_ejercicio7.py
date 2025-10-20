# Algoritmo para calcular la suma de los elementos de una lista usando recursividad
# Diego Emiliano Moran Trejo 

class SumaLista:
    def __init__(self, lista):
        self.lista = lista  

    def calcular(self, lista):
        if not lista:  
            return 0
        else:
            return lista[0] + self.calcular(lista[1:])  
    def imprimir(self):
        print(self.calcular(self.lista))  

objSuma = SumaLista([1, 2, 3, 4, 5])
objSuma.imprimir()  
print("Diego Emiliano Moran Trejo")
