usuarios = [
    ["chanchito", 4],
    ["Felipe", 1],
    ["pulga", 5]
]


nombre = []
for usuario in usuarios:
    nombre.append(usuario[0])
print(nombre)
# map
otro = [usuario[0] for usuario in usuarios]
print(otro)
# filter
vez = [usuario for usuario in usuarios if usuario[1] > 4]
print(vez)

#  map and filter
vez2 = [usuario[0] for usuario in usuarios if usuario[1] > 4]
print(vez2)
