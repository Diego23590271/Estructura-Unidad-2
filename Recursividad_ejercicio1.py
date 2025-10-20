# Algoritmo para calcular el factorial de un número usando recursividad
#Diego Emiliano Moran Trejo
"""
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))  # 120
"""
class Factorial: 
    def __init__(self,n ):
        self.n=n 
    
    def calcularFactorial(self, num ):
        if num == 1:
            return 1
        else:
            return num * self.calcularFactorial(num-1)

    def imprimir(self):
        print(self.calcularFactorial(self.n))

objfac = Factorial (5)
objfac.imprimir()

print("Diego Emiliano Moran Trejo")
