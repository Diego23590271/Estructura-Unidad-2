#EJERCICIO 6 invertir el orden de los digitos de un numero entero.
#Diego Emiliano Moran Trejo
import time
import tracemalloc

# MeMc: Medición de tiempo y memoria para invertir un número entero
tracemalloc.start()
start_time_ns = time.time_ns()

def contarDigitos(n):
    if type(n) != int or n < 0:
        raise Exception("n debe ser entero no negativo.")
    return contarDigitosAux(n)

def contarDigitosAux(n):
    if n < 10:
        return 1
    else:
        return contarDigitosAux(n // 10) + 1

def invertirEntero(n):
    if type(n) != int or n < 1:
        raise Exception("n debe ser entero positivo.")
    return invertirEnteroAux(n)

def invertirEnteroAux(n):
    if n < 10:
        return n
    else:
        return (n % 10) * 10**contarDigitos(n // 10) + invertirEnteroAux(n // 10)

resultado = invertirEntero(123456789)
print(f"Número invertido: {resultado}")

end_time_ns = time.time_ns()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Tiempo de ejecución: {end_time_ns - start_time_ns} nanosegundos")
print(f"Memoria actual usada: {current} bytes")
print(f"Pico máximo de memoria: {peak} bytes")
print("Diego Emiliano Moran Trejo")
