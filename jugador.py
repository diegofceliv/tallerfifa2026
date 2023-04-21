class Jugador:

    def __init__(self, nombre, fecha_nacimiento, posicion, estatura, peso):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.posicion = posicion
        self.estatura = estatura
        self.peso = peso

    def __str__(self):
        return self.nombre + ", " + self.posicion