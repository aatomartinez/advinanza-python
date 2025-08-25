nombre1 = input("Como se llamara el jugador1? ").title()
nombre2 = input("Como se llamara el jugador2? ").title()

sumador1 = 0
sumador2 = 0

while (sumador1 < 2 and sumador2 < 2):

    jugador1 = input(f"Que vas a elegir {nombre1}, piedra, papel o tijeras: ? ").lower()
    jugador2 = input(f"Que vas a elegir {nombre2}, piedra, papel o tijeras: ? ").lower()

    condicion1 = jugador1 == "piedra" and jugador2 == "tijeras"
    condicion2 = jugador1 == "papel" and jugador2 == "piedra"
    condicion3 = jugador1 == "tijeras" and jugador2 == "papel"

    if jugador1 == jugador2:
        print("Empate")
    elif condicion1 or condicion2 or condicion3:
        print("Ha ganado ", nombre1)
        sumador1 += 1

    else:
        print("Ha ganado ", nombre2)
        sumador2 += 1

    print(f"Marcador: {nombre1} {sumador1} - {nombre2} {sumador2}\n")