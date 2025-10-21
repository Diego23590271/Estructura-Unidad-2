#Diego Emiliano Moran Trejo
class ColaHospital:

    def __init__(self):

        self.cola = []

    def agregar_paciente(self, nombre, prioridad):

        if prioridad == 1:
            tipo = "Emergencia"
            salto = 3
        elif prioridad == 2:
            tipo = "Urgente"
            salto = 2
        else:
            tipo = "General"
            salto = 0 
        posicion = max(len(self.cola) - salto, 0)


        self.cola.insert(posicion, (nombre, tipo))

        print(f"{nombre} ({tipo}) fue agregado en la posición {posicion + 1}")

    def mostrar_orden(self):
        """Muestra el orden final de atención."""
        print("\nORDEN FINAL DE ATENCIÓN:\n")
        for turno, (nombre, tipo) in enumerate(self.cola, start=1):
            print(f"{turno}. Atendiendo a: {nombre} — Prioridad: {tipo}")


hospital = ColaHospital()

pacientes = [
    ("Laura", 3),
    ("Andrés", 2),
    ("Rosa", 1),
    ("Daniel", 3),
    ("Carmen", 2),
    ("José", 3),
    ("Luisa", 1),
    ("Miguel", 3),
    ("Pablo", 2),
    ("Elena", 1)
]

for nombre, prioridad in pacientes:
    hospital.agregar_paciente(nombre, prioridad)

hospital.mostrar_orden()
