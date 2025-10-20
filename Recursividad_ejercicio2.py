# Algoritmo para calcular la suma de los primeros n números naturales usando recursividad
#Diego Emiliano Moran Trejo

class Suma_natural:
    def __init__(self,n):
        self.n = n 
    
    def calcularsum (self, num):
        if num == 1:
            return 1
        else:
            return num + self.calcularsum(num-1)

    def imprimir (self):
        print(self.calcularsum(self.n))

objsuma = Suma_natural (5)
objsuma.imprimir()
print ("Diego Emiliano Moran Trejo")
