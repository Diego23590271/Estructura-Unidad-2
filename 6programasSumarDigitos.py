#EJERCICIO 5 sumar los digitos de un numero entero.
#Diego Emiliano Moran Trejo
import time
import tracemalloc

# MeMc: Medición de tiempo y memoria para sumar dígitos
tracemalloc.start()
start_time_ns = time.time_ns()

def sumarDigitos(n):
    if type(n) != int or n < 0:
        raise Exception("n debe ser entero no negativo.")
    return sumarDigitosAux(n)

def sumarDigitosAux(n):
    if n < 10:
        return n
    else:
        return sumarDigitosAux(n // 10) + n % 10

resultado = sumarDigitos(123456)
print(f"Suma de los dígitos: {resultado}")

end_time_ns = time.time_ns()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Tiempo de ejecución: {end_time_ns - start_time_ns} nanosegundos")
print(f"Memoria actual usada: {current} bytes")
print(f"Pico máximo de memoria: {peak} bytes")
print("Diego Emiliano Moran Trejo")
