from jugador import Jugador

class Seleccion:

    def __init__(self, nombre):
        self.nombre = nombre
        self.jugadores: Jugador = []

    def __str__(self):
        return self.nombre
    
    def agregarJugador(self, jugador):
        self.jugadores.append(jugador)