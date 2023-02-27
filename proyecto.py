#!/usr/bin/env python3
# Definir la clase Personaje
class Personaje:
    def __init__(self, nombre: str, tipo: str, valor: int, defensa: int, ataque: int, salud: int, estado: bool):
        self.nombre = nombre
        self.tipo = tipo
        self.valor = valor
        self.defensa = defensa
        self.ataque = ataque
        self.salud = salud
        self.estado = estado

# Definir la clase Ejercito
class Ejercito:
    def __init__(self, nombre: str, personajes: list):
        self.nombre = nombre
        self.personajes = personajes

# Crear una lista de personajes para el Ejército player1
#personajes_player1 = [Personaje("Gandalf", "Mago", 100, 50, 70, 80, True),
#                      Personaje("Bilbo Bolsón", "Débil", 20, 10, 10, 30, True),
#                      Personaje("Boromir", "Defensivo", 70, 70, 40, 80, True)]

# Crear la variable global player1 de tipo Ejército
global player1
#player1 = Ejercito("Ejército del Oeste", personajes_player1)


# Función para crear una galería de personajes
def crear_galeria():
    # Lista de personajes
    galeria = []
    
    # Personajes débiles
    personaje_debil_1 = Personaje("Bilbo Bolsón", "Débil", 20, 10, 10, 30, True)
    personaje_debil_2 = Personaje("Sam Gamyi", "Débil", 25, 12, 12, 35, True)
    galeria.append(personaje_debil_1)
    galeria.append(personaje_debil_2)

    # Personajes ofensivos
    personaje_ofensivo_1 = Personaje("Legolas", "Ofensivo", 80, 20, 70, 60, True)
    personaje_ofensivo_2 = Personaje("Gimli", "Ofensivo", 75, 25, 65, 65, True)
    galeria.append(personaje_ofensivo_1)
    galeria.append(personaje_ofensivo_2)
    
    # Personajes defensivos
    personaje_defensivo_1 = Personaje("Boromir", "Defensivo", 70, 70, 40, 80, True)
    personaje_defensivo_2 = Personaje("Faramir", "Defensivo", 65, 65, 35, 75, True)
    galeria.append(personaje_defensivo_1)
    galeria.append(personaje_defensivo_2)
    
    # Personajes destructivos
    personaje_destructivo_1 = Personaje("Gandalf", "Destructivo", 90, 50, 80, 90, True)
    personaje_destructivo_2 = Personaje("Saruman", "Destructivo", 85, 45, 75, 85, True)
    galeria.append(personaje_destructivo_1)
    galeria.append(personaje_destructivo_2)
    
    # Devolver la lista de personajes
    return galeria

# Función para imprimir la galería de personajes
def imprimir_galeria(galeria):
    for personaje in galeria:
        print(f"Nombre: {personaje.nombre}")
        print(f"Tipo: {personaje.tipo}")
        print(f"Valor: {personaje.valor}")
        print(f"Defensa: {personaje.defensa}")
        print(f"Ataque: {personaje.ataque}")
        print(f"Salud: {personaje.salud}")
        print(f"Estado: {personaje.estado}")
        print("")
        

def imprimir_equipo():
    for personaje in personajes_player1:
        if personaje.salud >= 50:
            print(personaje.nombre)
            print(personaje.valor)
            print("Estado: Vivo")
        else:
            print(personaje.nombre)
            print(personaje.valor)
            print("Estado: Muerto")

def menu_elegir_personaje():
    print("Bienvenido al menú de selección de personajes.")
    print("Los personajes disponibles son:")
    for i, personaje in enumerate(galeria):
        if personaje.estado == True:
            print(f"{i + 1}. {personaje.nombre} ({personaje.tipo}) ({personaje.estado})")
    jugadores = []
    valor_total = 0
    max_jugadores = 4

    while len(jugadores) < max_jugadores and valor_total < 200:
        opcion = input("Elige un personaje escribiendo su número (o 'q' para salir): ")

        if opcion.lower() == "q":
            print("¡Hasta la próxima!")
            return None

        try:
            opcion = int(opcion)
        except ValueError:
            print("Opción inválida. Por favor, introduce un número o 'q' para salir.")
            continue

        if opcion < 1 or opcion > len(galeria):
            print("Opción inválida. Por favor, elige un número de la lista.")
            continue

        personaje_elegido = galeria[opcion - 1]
        
        if not personaje_elegido.estado:
            print("Ese personaje ya ha sido elegido. Por favor, elige otro.")
            continue

        jugadores.append(personaje_elegido)
        valor_total += personaje_elegido.valor    
        personaje_elegido.estado = False
        print(f"Has elegido a {personaje_elegido.nombre} ({personaje_elegido.tipo}) ({personaje_elegido.estado})")
        print(f"El valor total de los personajes elegidos es {valor_total}.")
        print(len(jugadores))
        return personaje_elegido
    

# Programa principal


#imprimir_galeria(galeria)
#imprimir_equipo()
galeria = crear_galeria()
menu_elegir_personaje()


# Continuar con el juego...

