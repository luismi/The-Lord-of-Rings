#!/usr/bin/env python3

# Lista vacía para almacenar los soldados elegidos por el jugador
ejercito_player1 = []
ejercito_player2 =[]
# Pedir al jugador que ingrese su nombre
jugador1 = input("Ingrese su nombre: ")
jugador2 = input("Ingrese su nombre: ")
#Ejercito1 ={'nombre:':jugador1, ejercito_player1}

soldado1 = {'nombre': 'Debil', 'valor': 25, 'ataque': 1,'defensa': 1,'salud': 50, 'estado' :True}
soldado2 = {'nombre': 'Ofensivo', 'valor': 250, 'ataque': 2,'defensa': 4,'salud': 50, 'estado' :True}
soldado3 = {'nombre': 'Defensivo', 'valor': 250, 'ataque': 4,'defensa': 2,'salud': 50, 'estado' :True}
soldado4 = {'nombre': 'Destructor', 'valor': 450, 'ataque': 3,'defensa': 5,'salud': 50, 'estado' :True}
puntos_disponibles1 = 1000
puntos_disponibles2 = 1000
soldados_disponibles = [soldado1, soldado2, soldado3, soldado4]


def menu_campo():   
    print("===================================================")
    print("         CAMPO DE BATALLA           ")
    print("===================================================")
    for j, soldado in enumerate(soldados_disponibles):
        print(f"{j+1}. {soldado['nombre']} (valor: {soldado['valor']})")
    print("----------------------------------------------------")
    #for (i=0;i<MIEM_EJER;i++)
    #{
    #    cout <<"["<<i<<"] " << players1.miembros[i].nombre << " Ps:" << players1.miembros[i].salud  << "\t\t["<<i<<"] "
    #    << players2.miembros[i].nombre << " Ps:" << players2.miembros[i].salud << endl;
    #}
    print("----------------------------------------------------")

def imprimir_galeria():
    # Mostrar soldados disponibles y puntos disponibles
    for j, soldado in enumerate(soldados_disponibles):
            print(f"{j+1}. {soldado['nombre']} (valor: {soldado['valor']})")

def pedir_player1():
    global puntos_disponibles1
    # Pedir al jugador que seleccione 5 soldados
    for i in range(5):
        # Pedir al jugador que seleccione un soldado
        while True:
            try:
                seleccion = int(input("Seleccione un soldado (1-5): "))
                if seleccion < 1 or seleccion > 5:
                    print("Selección inválida, por favor seleccione un número entre 1 y 5")
                elif soldados_disponibles[seleccion-1]['valor'] >  puntos_disponibles1:
                    print("No tiene suficientes puntos disponibles para seleccionar este soldado")
                else:
                    # Pedir al jugador que seleccione la posición del soldado en el ejército
                    posicion = int(input("Seleccione la posición del soldado en el ejército (1-5): "))
                    if posicion < 1 or posicion > 5:
                        print("Posición inválida, por favor seleccione un número entre 1 y 5")
                    else:
                        # Insertar soldado en la posición seleccionada y restar su costo a los puntos disponibles
                        ejercito_player1.insert(posicion-1, soldados_disponibles[seleccion-1])
                        puntos_disponibles1 -= soldados_disponibles[seleccion-1]['valor']
                        break
            except ValueError:
                print("Selección inválida, por favor seleccione un número entre 1 y 5")
            print(f"Puntos disponibles: {puntos_disponibles1}")
     
    print("Ejército configurado:")
    print(f"Puntos disponibles: {puntos_disponibles1}")

def pedir_player2():
    # Pedir al jugador que seleccione 5 soldados
    for i in range(5):
        # Pedir al jugador que seleccione un soldado
        while True:
            try:
                seleccion = int(input("Seleccione un soldado (1-5): "))
                if seleccion < 1 or seleccion > 5:
                    print("Selección inválida, por favor seleccione un número entre 1 y 5")
                elif soldados_disponibles[seleccion-1]['valor'] > puntos_disponibles2:
                    print("No tiene suficientes puntos disponibles para seleccionar este soldado")
                else:
                    # Añadir soldado a la lista del ejército y restar su costo a los puntos disponibles
                    ejercito_player2.append(soldados_disponibles[seleccion-1])
                    puntos_disponibles2 -= soldados_disponibles[seleccion-1]['valor']
                    break
            except ValueError:
                print("Selección inválida, por favor seleccione un número entre 1 y 5")      
    print("Ejército configurado:")
    for soldado in ejercito_player2:
        print(soldado['nombre'])
    print(f"Puntos disponibles: {puntos_disponibles2}")

def imprimir_equipo1():
    for soldado in ejercito_player1:
        print(soldado['nombre'])
    print(f"Puntos disponibles: {puntos_disponibles1}")

    # Mostrar opciones disponibles
    print("-----------------------------------")
    print("Creando ejercito jugador: ", jugador1)
    print("-----------------------------------")
    print("Puntos disponibles: ", puntos_disponibles1)
    print("-----------------------------------")
    print("1 - Agregar/modificar soldado")
    print("2 - Cargar ejercito basico")
    print("0 - Equipo terminado")
    print("Opcion: ")
    # Pedir al jugador que seleccione una opción
    seleccion = input("Seleccione una opción (1-3): ")
    

# Programa principal

while True:

    imprimir_galeria()
    print("-----------------------------------")
    imprimir_equipo1()
    
    # Ejecutar la acción correspondiente a la selección del jugador
    # Pedir al jugador que seleccione una opción
    seleccion = input("Seleccione una opción (1-3): ")
    if seleccion == "1":
        pedir_player1()
        imprimir_equipo1()
    elif seleccion == "0":
        break
        

