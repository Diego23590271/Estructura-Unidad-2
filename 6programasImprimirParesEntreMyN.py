#EJERCICIO 2 imprimir los numeros impares entre dos enteros M y N con M<N.
#Diego Emiliano Moran Trejo
import time
import tracemalloc

# MeMc: Medición de tiempo y memoria para imprimir impares entre m y n
tracemalloc.start()
start_time_ns = time.time_ns()

def imprimirImparesEntreMyN(m, n):
    if type(m) != int:
        raise Exception("m debe ser entero positivo.")
    if type(n) != int or n <= m:
        raise Exception("n debe ser entero positivo y mayor que m.")
    m = m + 1 if m % 2 == 0 else m
    n = n - 1 if n % 2 == 0 else n
    imprimirImparesEntreMyNAux(m, n)
    print()

def imprimirImparesEntreMyNAux(m, n):
    if m > n:
        return
    else:
        print(m, end=" ")
        imprimirImparesEntreMyNAux(m + 2, n)

imprimirImparesEntreMyN(2, 8)

end_time_ns = time.time_ns()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"\nTiempo de ejecución: {end_time_ns - start_time_ns} nanosegundos")
print(f"Memoria actual usada: {current} bytes")
print(f"Pico máximo de memoria: {peak} bytes")
