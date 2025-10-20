# Algoritmo para verificar si una palabra es palíndromo usando recursividad
# Diego Emiliano Moran Trejo
"""
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])

print(es_palindromo("anilina"))  # True
"""
class Palindromo:
    def __init__(self, palabra):
        self.palabra = palabra  

    def calcular(self, palabra):
        if len(palabra) <= 1: 
            return True
        elif palabra[0] != palabra[-1]:  
            return False
        else:
            return self.calcular(palabra[1:-1])  

    def imprimir(self):
        print(self.calcular(self.palabra)) 

objPal = Palindromo("anilina")
objPal.imprimir()  # Resultado: True
print("Diego Emiliano Moran Trejo")
