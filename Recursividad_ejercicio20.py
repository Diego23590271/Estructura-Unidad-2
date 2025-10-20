# Algoritmo para generar todas las permutaciones de una lista usando recursividad
# Diego Emiliano Moran Trejo

"""
def permutaciones(lista, inicio=0):
    if inicio == len(lista) - 1:
        print(lista)
    else:
        for i in range(inicio, len(lista)):
            lista[inicio], lista[i] = lista[i], lista[inicio]
            permutaciones(lista, inicio + 1)
            lista[inicio], lista[i] = lista[i], lista[inicio]

permutaciones([1, 2, 3])
"""
class Permutaciones:
    def __init__(self, lista):
        self.lista = lista  

    def calcular(self, lista, inicio=0):
        if inicio == len(lista) - 1:  
            print(lista)  
        else:
            for i in range(inicio, len(lista)):
                lista[inicio], lista[i] = lista[i], lista[inicio]  
                self.calcular(lista, inicio + 1)  
                lista[inicio], lista[i] = lista[i], lista[inicio]  
    def imprimir(self):
        self.calcular(self.lista) 

objPermutaciones = Permutaciones([1, 2, 3])
objPermutaciones.imprimir()
print("Diego Emiliano Moran Trejo")
