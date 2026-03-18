def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """

    decimal=float(input("Ingresar gasto:\n"))
    entero=int(input("Dinero recibido\n"))

    print("Ingresar gasto:")
    print(decimal)
    print("Dinero recibido")
    print(entero)
    total = int(entero - decimal)
    centavos_entero= int(decimal)
    centavos = (1-(decimal - centavos_entero )) * 100

    print("\nVuelto\n")
    print("Pesos:")
    print(total)
    print("Centavos:")
    print(round(centavos))
