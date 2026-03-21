def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """
    pass

    nombre=input()
    appelido= input()
    min= nombre.lower() + " " + appelido.lower()
    tit= nombre.title() + " " + appelido.title()
    may= nombre.upper() + " " + appelido.upper()
    tab= "\t" + nombre.lower() + " " + appelido.lower()

    print(min)
    print(tit)
    print(may)
    print(tab)
