"""
Ejercicio de práctica en Python
Tema: Lista + Diccionario + Condicional + Bucle
Nivel: Básico
"""
"""
Enunciado:
Crea un diccionario llamado productos con 3 productos y sus precios.
Crea una lista vacía llamada carrito.
Recorre el diccionario y muestra los productos disponibles.
Permite al usuario escribir el nombre de un producto para agregarlo al carrito.
Si el producto existe:
- Agrégalo a la lista carrito.
Si no existe:
- Muestra un mensaje de error.
Al final, muestra el contenido del carrito.
"""
productos = {"chicle":1,"manzanas":3,"pilas":2}
carrito =[]
print("Los productos són lo siguientres:")
for producto in productos:
    print(producto)
producto = input("Por favor ingrese el nombre de un producto o tecle salir para finalizar: ")
while producto != "salir" :
    if producto in productos:
        carrito.append(producto)
        print("Producto agregado")
    else:
        print("Producto no existe")
    producto = input("Por favor ingrese el nombre de un producto o tecle salir para finalizar: ")
print("Los productos agrados al carrito són:",carrito)