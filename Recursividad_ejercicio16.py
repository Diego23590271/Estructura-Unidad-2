# Algoritmo para imprimir una pirámide de asteriscos usando recursividad
#Diego Emiliano Moran Trejo

"""
def piramide(n):
    if n == 0:
        return
    piramide(n-1)
    print('*' * n)

piramide(5)
"""
class Piramide:
    def __init__(self, n):
        self.n = n  

    def calcular(self, n):
        if n == 0:  
            return
        self.calcular(n - 1)  
        print('*' * n)  
    def imprimir(self):
        self.calcular(self.n)  

objPiramide = Piramide(5)
objPiramide.imprimir()
print("Diego Emiliano Moran Trejo")
