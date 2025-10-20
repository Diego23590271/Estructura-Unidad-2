# Algoritmo para calcular el n-ésimo número de Fibonacci usando recursividad
# Diego Emiliano Moran Trejo
"""
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))  # 8
"""
class Fibonacci:
    def __init__(self,num1):
        self.num1 = num1

    def calcularFibo(self,num1):
        if num1 == 0 or num1 == 1:
            return num1
        else:
            return self.calcularFibo(num1-1) + self.calcularFibo(num1-2)
        
    def imprimir(self):
        print(self.calcularFibo(self.num1)) 

objFibo =Fibonacci(6)
objFibo.imprimir()
print("Diego Emiliano Moran Trejo ")
