"""
Ejercicio de práctica en Python
Tema: Diccionarios
Nivel: Básico
"""
"""
Crea un diccionario llamado usuario con las claves:
"nombre"
"email"
"edad"
"pais"
Muestra el diccionario.
Pide al usuario que ingrese una clave que quiera eliminar.
Si la clave existe:
- Elimínala usando pop()
- Muestra el valor eliminado
- Muestra el diccionario actualizado
Si la clave no existe:
- Muestra un mensaje de error.
"""
usuario = {"email":"usuario132@gmail.com","edad":23,"pais":"España"}
clave = input("Por favor ingrese una clave: ")
if clave in usuario:
    print("El valor eliminado es:",usuario.pop(clave))
    print(usuario)
else:
    print("No encontrado")