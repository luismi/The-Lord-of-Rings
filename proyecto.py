#!/usr/bin/env python3

# Lista vacía para almacenar los soldados elegidos por el jugador
ejercito_player1 = []
ejercito_player2 =[]
# Pedir al jugador que ingrese su nombre
jugador = input("Ingrese su nombre: ")

soldado1 = {'nombre': 'Debil', 'valor': 25, 'ataque': 1,'defensa': 1,'salud': 50, 'estado' :True}
soldado2 = {'nombre': 'Ofensivo', 'valor': 250, 'ataque': 2,'defensa': 4,'salud': 50, 'estado' :True}
soldado3 = {'nombre': 'Defensivo', 'valor': 250, 'ataque': 4,'defensa': 2,'salud': 50, 'estado' :True}
soldado4 = {'nombre': 'Destructor', 'valor': 450, 'ataque': 3,'defensa': 5,'salud': 50, 'estado' :True}

soldados_disponibles = [soldado1, soldado2, soldado3, soldado4]


def pedir_player1():
    puntos_disponibles = 1000
    # Pedir al jugador que seleccione 5 soldados
    for i in range(5):
        # Mostrar soldados disponibles y puntos disponibles
        print(f"Soldados disponibles (puntos disponibles: {puntos_disponibles}):")
        for j, soldado in enumerate(soldados_disponibles):
            print(f"{j+1}. {soldado['nombre']} (valor: {soldado['valor']})")
        
        # Pedir al jugador que seleccione un soldado
        while True:
            try:
                seleccion = int(input("Seleccione un soldado (1-5): "))
                if seleccion < 1 or seleccion > 5:
                    print("Selección inválida, por favor seleccione un número entre 1 y 5")
                elif soldados_disponibles[seleccion-1]['valor'] > puntos_disponibles:
                    print("No tiene suficientes puntos disponibles para seleccionar este soldado")
                else:
                    # Añadir soldado a la lista del ejército y restar su costo a los puntos disponibles
                    ejercito_player1.append(soldados_disponibles[seleccion-1])
                    puntos_disponibles -= soldados_disponibles[seleccion-1]['valor']
                    break
            except ValueError:
                print("Selección inválida, por favor seleccione un número entre 1 y 5")      
    print("Ejército configurado:")
    for soldado in ejercito_player1:
        print(soldado['nombre'])
    print(f"Puntos disponibles: {puntos_disponibles}")

def pedir_player2():
    puntos_disponibles = 1000
    # Pedir al jugador que seleccione 5 soldados
    for i in range(5):
        # Mostrar soldados disponibles y puntos disponibles
        print(f"Soldados disponibles (puntos disponibles: {puntos_disponibles}):")
        for j, soldado in enumerate(soldados_disponibles):
            print(f"{j+1}. {soldado['nombre']} (valor: {soldado['valor']})")
        
        # Pedir al jugador que seleccione un soldado
        while True:
            try:
                seleccion = int(input("Seleccione un soldado (1-5): "))
                if seleccion < 1 or seleccion > 5:
                    print("Selección inválida, por favor seleccione un número entre 1 y 5")
                elif soldados_disponibles[seleccion-1]['valor'] > puntos_disponibles:
                    print("No tiene suficientes puntos disponibles para seleccionar este soldado")
                else:
                    # Añadir soldado a la lista del ejército y restar su costo a los puntos disponibles
                    ejercito_player2.append(soldados_disponibles[seleccion-1])
                    puntos_disponibles -= soldados_disponibles[seleccion-1]['valor']
                    break
            except ValueError:
                print("Selección inválida, por favor seleccione un número entre 1 y 5")      
    print("Ejército configurado:")
    for soldado in ejercito_player2:
        print(soldado['nombre'])
    print(f"Puntos disponibles: {puntos_disponibles}")


# Programa principal

while True:
    # Mostrar opciones disponibles
    print(f"\n--- Menú ---")
    print("1. Configurar ejército player1")
    print("2. Configurar ejército player2")
    print("3. Salir")
    
    # Pedir al jugador que seleccione una opción
    seleccion = input("Seleccione una opción (1-3): ")
    
    # Ejecutar la acción correspondiente a la selección del jugador
    if seleccion == "1":
        pedir_player1()
    elif seleccion == "2":
        pedir_player2()


