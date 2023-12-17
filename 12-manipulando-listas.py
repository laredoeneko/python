mascotas = ["cesar", "bravo", "del", "alamo"]

print(mascotas[1])

mascotas[0] = "hombre"
print(mascotas[0])
print(mascotas[2:])
print(mascotas[-1])  # empieza por el final
print(mascotas[::2])   # para coger uno si uno no
print(mascotas[1::2])


numeros = list(range(21))
print(numeros)
print(numeros[1::2])   # obtiene los impares
print(numeros[0::2])  # obtiene los impares
