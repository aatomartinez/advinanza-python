
 #Calcular el area de un circulo teniendo el radio

# Solicitar que ingresen el radio del circulo

from math import pi


radio = float(input("Ingrese un radio para calcular el area del circulo: "))

area = pi * (radio**2)

print(f"El area del circulo es {area:.2f}")