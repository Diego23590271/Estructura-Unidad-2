#EJERCICIO 3 suamr todos los numeros pares de una lista de enteros. 
#Diego Emiliano Moran Trejo
import time
import tracemalloc

# MeMc: Medición de tiempo y memoria para sumar pares hasta N
tracemalloc.start()
start_time_ns = time.time_ns()

def sumarPares(n):
    if type(n) != int or n < 3:
        raise Exception("n debe ser entero positivo.")
    n -= n % 2
    return sumarParesAux(n)

def sumarParesAux(n):
    if n == 0:
        return 0
    else:
        return sumarParesAux(n - 2) + n

resultado = sumarPares(8)
print(f"Suma de pares hasta 8: {resultado}")

end_time_ns = time.time_ns()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Tiempo de ejecución: {end_time_ns - start_time_ns} nanosegundos")
print(f"Memoria actual usada: {current} bytes")
print(f"Pico máximo de memoria: {peak} bytes")
print("Diego Emiliano Moran")
