numeros = [1, 2, 3, 4]


primero = numeros[0]
segundo = numeros[1]
tercero = numeros[2]


# primero, segundo, tercero, cuarto = numeros
primero, *otros = numeros

print(primero)
print(otros)


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
primero, segundo, *otros, ultimo = numeros
print(primero, segundo, otros, ultimo)


for a in otros:
    print(a)
