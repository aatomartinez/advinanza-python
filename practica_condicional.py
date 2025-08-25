
#El usuario quiere saber si puede entrar a una discoteca segun la edad del cliente

edad = int(input("Ingresa la edad del cliente: "))
permitido = edad >= 18
print("Podes ingresar" if permitido else "No podes ingresar")