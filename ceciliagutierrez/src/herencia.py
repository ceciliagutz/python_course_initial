class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class SuperHeroe(Persona):
    def __init__(self, nombre, puesto):
        super().__init__(nombre)
        self.puesto = puesto

    def __str__(self):
        return f"Princesas {self.nombre}"

empleado = SuperHeroe("Cecilia", "Trainee")

print(empleado)