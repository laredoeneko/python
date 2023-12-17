mascotas = ["pelusa", "pulga", "pajaro", "cesar"]


for mascota in mascotas:
    print(mascota)

print("--------------------")
for mascota in enumerate(mascotas):
    # print(mascota)    # tupla de elementos
    print(mascota[0], mascota[1])
