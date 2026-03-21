def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """
    pass

    nombre=input()
    min= nombre.lower()
    tit= nombre.title()
    may= nombre.upper()
    tab= "\t" + nombre.lower()

    print(min)
    print(tit)
    print(may)
    print(tab)
