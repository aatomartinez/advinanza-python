import random

numero_secreto = random.randint(0,100)
adivinado = False
cantIntentos = 0
cantMaxIntentos = 5
print("Bienvenido al juego de adivinar el numero secreto")

while not adivinado and cantIntentos < cantMaxIntentos:
    numero = int(input("Intoduce un numero del 1 al 99: ")) 

    if numero == numero_secreto:
        print("Felicitaciones, adivinaste")
        adivinado = True
    elif numero < numero_secreto:
        print(f"El numero es mayor al ingresado, te quedan {cantMaxIntentos - cantIntentos - 1} intentos")
    else:
        print(f"El numero es menor al ingresado, te quedan {cantMaxIntentos - cantIntentos - 1} intentos")
    
    cantIntentos += 1

if cantIntentos == cantMaxIntentos:
    print("Perdiste, te quedaste sin intentos, eran 5 intentos")