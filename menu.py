import os

from jugador import Jugador
from seleccion import Seleccion

selecciones = [Seleccion("Alemania"),
               Seleccion("Argentina"),
               Seleccion("Brasil"),
               Seleccion("Colombia"),
               Seleccion("España"),
               Seleccion("Francia"),
               Seleccion("Inglaterra"),
               Seleccion("Mexico"),
               Seleccion("Polonia"),
               Seleccion("Portugal")]

#España
selecciones[4].agregarJugador(Jugador("Unai Simón", "5/2/1985", "Portero", 189, 85))
selecciones[4].agregarJugador(Jugador("Robert Sánchez", "5/2/1985", "Portero", 189, 85))

os.system('clear')
print("Bienvenido a la Copa Mundo 2026")

print("Escoga un equipo")

i = 0
for seleccion in selecciones:
    i = i+1
    print(str(i) + ": " + str(seleccion))

eligio = int(input(""))

os.system('clear')
seleccionActual = selecciones[eligio-1]
print("Eligio " + str(seleccionActual))

opcion = input("""
Escoga una opción:
1. Ver jugadores
2. Agregar jugador
3. Eliminar jugador
4. Modificar jugador
5. Regresar
""")

while (opcion != "0"):
    os.system('clear')
    if opcion=="1":
        print("Lista de jugadores de " + seleccionActual.nombre)
        for jugador in seleccionActual.jugadores:
            print(jugador)
    elif opcion=="2":
        nombre = input("Escriba el nombre: ")
        posicion = input("Escriba el posicion: ")
        estatura = int(input("Escriba el estatura: "))
        peso = int(input("Escriba el peso: "))
        jugadorNuevo = Jugador(nombre, "", posicion, estatura, peso)
        seleccionActual.agregarJugador(jugadorNuevo)
    elif opcion=="3":
        print("Lista de jugadores")
        j = 0
        for jugador in seleccionActual.jugadores:
            j = j+1
            print(str(j) + ": " + str(jugador))
        eliminar = int(input("Digite el numero del jugador que desea eliminar"))
        del seleccionActual.jugadores[eliminar-1]
    elif opcion=="4":
        print("Lista de jugadores")
        j = 0
        for jugador in seleccionActual.jugadores:
            j = j+1
            print(str(j) + ": " + str(jugador))
        eliminar = input("Digite el numero del jugador que desea modificar")
    elif opcion=="5":
        print("Escoga un equipo")

        i = 0
        for seleccion in selecciones:
            i = i+1
            print(str(i) + ": " + str(seleccion))

        eligio = int(input(""))

        seleccionActual = selecciones[eligio-1]
        print("Eligio " + str(seleccionActual))
    else:
        print("Opción no válida")

    opcion = input("""
Escoga una opción:
1. Ver jugadores
2. Agregar jugador
3. Eliminar jugador
4. Modificar jugador
5. Regresar
""")

