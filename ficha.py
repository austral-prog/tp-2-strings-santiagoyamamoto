from gettext import find


def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)
    pass

    nombre=input("Ingrese su nombre completo: ").lower()
    email=input("Ingrese su email: ")
    nota1= int(input("Ingrese la primer nota: "))
    nota2 = int(input("Ingrese la segunda nota: "))
    nota3 = int(input("Ingrese la tercer nota: "))

    multilinea= """========================
    FICHA DEL ALUMNO
========================"""

    print(multilinea)
    print(f"Nombre: {nombre.strip().title()}")
    print(f"Email: {email.strip().lower()}")
    print(f"Caracteres en nombre: {len(nombre)}")

    lugar= int(nombre.find(" "))

    print(f"Iniciales: {nombre[0].upper()+nombre[lugar+1].upper()}")
    print(f"Usuario: {nombre.lower()[lugar+1:] + "." + nombre.lower()[:lugar] }")
    print(f"Email valido: {"@" in email}")

    arroba= email.find("@")

    print(f"Dominio: {email[arroba+1:].lower()}")
    print(f"Nombre para archivo: {nombre.replace(" ", "_").title()}")
    print(f"Cantidad de a: {nombre.count("a")}")
    print(f"Codigo secreto: {nombre[::-1].upper()}")
    print(f"Nota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    print(f"Nota 3: {nota3}")

    suma= nota1 + nota2 + nota3

    print(f"Suma: {suma}")
    print(f"Promedio: {suma/3}")
    print(f"Promedio entero: {suma//3}")
    print("="*24)

