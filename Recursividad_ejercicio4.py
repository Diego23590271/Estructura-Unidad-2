# Algoritmo para calcular la potencia de un número usando recursividad
#Diego Emiliano Moran Trejo

"""
def potencia(a, b):
    if b == 0:
        return 1
    else:
        return a * potencia(a, b-1)

print(potencia(2, 3))  # 8
"""

class Potencial:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def calcularPote(self,num1,num2):
        if num2 == 0:
            return 1
        else:
            return num1 * self.calcularPote(num1, num2-1)
        
    def imprimir(self):
        print(self.calcularPote(self.num1, self.num2)) 

objPot = Potencial (2,3)
objPot.imprimir()
print("Diego Emiliano Moran Trejo")
