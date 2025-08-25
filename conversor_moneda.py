
cambio = input("Seleccione si quiere convertir USD o EUR : " )
dinero = float(input("Seleccione la cantidad de dinero a depositar : " ))

euro = 0.6
dolar = 0.5

if cambio.upper() == "EUR":
    print("El cambio es ", dinero * euro)
elif cambio.upper() == "USD":
    print("El cambio es ", dinero * dolar)
else:
    print("No esta diponible actualmente esa divisa")
