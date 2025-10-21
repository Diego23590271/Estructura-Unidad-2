#EJERCICIO 1 imprimir los numeros pares desde 2 hasta un entero positivo N.
#Diego Emiliano Moran Trejo
import time
import tracemalloc  

# MeMc: Medición de tiempo y memoria para imprimir pares hasta N
tracemalloc.start()  
start_time_ns = time.time_ns()  

def imprimirParesHastaN(n):
    if type(n) != int or n < 1: 
        raise Exception("n debe ser entero positivo.")
    n -= n % 2   
    imprimirParesHastaNAux(n)
    print()

def imprimirParesHastaNAux(n):
    if n == 0: 
        return
    else: 
        imprimirParesHastaNAux(n - 2)
        print(n, end=" ")

imprimirParesHastaN(8)

end_time_ns = time.time_ns() 
current, peak = tracemalloc.get_traced_memory()  
tracemalloc.stop()  
# Resultados
print(f"\nTiempo de ejecución: {end_time_ns - start_time_ns} nanosegundos")
print(f"Memoria actual usada: {current} bytes")
print(f"Pico máximo de memoria: {peak} bytes")
print("Diego Emiliano Moran Trjeo")
