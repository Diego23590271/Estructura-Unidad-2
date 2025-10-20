# Algoritmo para verificar si un número es primo usando recursividad
#Diego Emiliano Moran Trejo

"""
def es_primo(n, divisor=2):
    if n <= 2:
        return n == 2
    if n % divisor == 0:
        return False
    if divisor * divisor > n:
        return True
    return es_primo(n, divisor+1)

print(es_primo(13))  # True
"""
class EsPrimo:
    def __init__(self, n):
        self.n = n  

    def calcular(self, n, divisor=2):
        if n <= 2:  
            return n == 2
        if n % divisor == 0:  
            return False
        if divisor * divisor > n:  
            return True
        return self.calcular(n, divisor + 1)  

    def imprimir(self):
        print(self.calcular(self.n))  

objPrimo = EsPrimo(13)
objPrimo.imprimir()  
print("Diego Emiliano Moran Trejo")
