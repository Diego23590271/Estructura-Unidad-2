# Algoritmo para contar la cantidad de dígitos de un número usando recursividad
#Diego Emiliano Moran Trejo
"""
def contar_digitos(n):
    if n < 10:
        return 1
    else:
        return 1 + contar_digitos(n // 10)

print(contar_digitos(12345))  # 5
"""

class Contar_digitos:
    def __init__(self,n):
        self.n = n
    
    def calcular(self,num):
        if num < 10:
            return 1
        else:
            return 1 + self.calcular(num // 10)
        
    def imprimir(self):
        print(self.calcular(self.n))

objcon = Contar_digitos (12345)
objcon.imprimir()
print("Diego Emiliano Moran Trejo")
