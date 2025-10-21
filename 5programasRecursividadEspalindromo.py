#Diego Emiliano Moran Trejo

def es_palindromo(s: str) -> bool:
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return es_palindromo(s[1:-1])


def es_palindromo_normalizado(s: str) -> bool:
    t = ""
    for ch in s:
        if not ch.isspace():   # quita espacios
            t += ch.lower()    # pasa a minúsculas
    return es_palindromo(t)

while True:
    print("\n=== MENÚ PALÍNDROMOS ===")
    print("1. Verificar palíndromo exacto")
    print("2. Verificar palíndromo (ignorando espacios y mayúsculas)")
    print("3. Salir")

    opcion = input("Elige una opción (1-3): ")

    if opcion == "1":
        texto = input("Escribe una palabra o frase: ")
        print("¿Es palíndromo exacto?", es_palindromo(texto))

    elif opcion == "2":
        texto = input("Escribe una palabra o frase: ")
        print("¿Es palíndromo normalizado?", es_palindromo_normalizado(texto))

    elif opcion == "3":
        print("¡Hasta luego! ")
        break

    else:
        print("Opción no válida, intenta de nuevo.")
