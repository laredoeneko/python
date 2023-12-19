mascotas = ["pelusa", "pulga", "pajaro", "cesar", "Wolgang", "Wolgang"]

print(mascotas.count("Wolgang"))    # aparece 2 veces

if "Wolgang" in mascotas:   # comprueba que el elemento esta en la lista
    print(mascotas.index("Wolgang"))
