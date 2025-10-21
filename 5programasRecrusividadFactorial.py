#Diego Emiliano Moran Trejo

def factorial(n: int) -> int: 
    """ 
    Calcula n! recursivamente. 
    Precondición: n >= 0 
    """ 
    if n < 0: 
        raise ValueError("factorial: n debe ser >= 0") 
    if n == 0 or n == 1: 
        return 1 
    return n * factorial(n - 1)

print(factorial(0))  
print(factorial(1))  
print(factorial(5))  
print("Diego Emiliano Moran Trejo")
