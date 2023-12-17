def get_product(**datos):
    print(datos)
    print(datos["id"], datos["name"])


get_product(id="id", name="iPhone", desc="esto es un iphone")
