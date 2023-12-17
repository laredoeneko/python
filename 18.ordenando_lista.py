numeros = [2, 4, 1, 56, 6, 8, 67]

numeros.sort()
print(numeros)
numeros.sort(reverse=True)
print(numeros)

lista = sorted(numeros, reverse=True)  # devuelve una nueva lista
print("numeros with sorted", lista)


usuarios = [[2, "cesar"], [4, "felipe"], [5, "pulga"]]
usuarios.sort()
print(usuarios)
