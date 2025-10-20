# Algoritmo para resolver las Torres de Hanoi usando recursividad
#Diego Emiliano Moran Trejo

"""
def hanoi(n, origen, destino, auxiliar):
    if n == 1:
        print(f"Mover disco de {origen} a {destino}")
    else:
        hanoi(n-1, origen, auxiliar, destino)
        hanoi(1, origen, destino, auxiliar)
        hanoi(n-1, auxiliar, destino, origen)

hanoi(3, "A", "C", "B")
"""
class TorresHanoi:
    def __init__(self, n, origen, destino, auxiliar):
        self.n = n            
        self.origen = origen  
        self.destino = destino  
        self.auxiliar = auxiliar  
    def calcular(self, n, origen, destino, auxiliar):
        if n == 1:  
            print(f"Mover disco de {origen} a {destino}")
        else:
            self.calcular(n-1, origen, auxiliar, destino)
            self.calcular(1, origen, destino, auxiliar)
            self.calcular(n-1, auxiliar, destino, origen)

    def imprimir(self):
        self.calcular(self.n, self.origen, self.destino, self.auxiliar)  

objHanoi = TorresHanoi(3, "A", "C", "B")
objHanoi.imprimir()
print("Diego Emiliano Moran Trejo")
