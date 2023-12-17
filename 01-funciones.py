print("hola mundo")


def hola(hombre, apellidos="por defecto"):
    print("hola mundo")
    print(f"{hombre},{apellidos}")


hola(123, "bravo")
hola(123)


hola(apellidos="bravo", hombre="cesar")
