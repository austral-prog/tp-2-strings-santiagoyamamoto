def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    pass

    precio=int(input())
    descuento=float(input())
    cantidad=int(input())

    print(f"Precio: {precio}")
    print(f"Descuento: {descuento}")
    print(f"Precio con descuento: {precio-descuento}")
    print(f"Total: {(precio-descuento)*cantidad}")
