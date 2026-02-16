"""
Ejercicio de práctica en Python
Tema: Set + Validación + While
Nivel: Básico
"""
"""
Enunciado:
Crea un conjunto vacío llamado usuarios.
Usa un while que permita ingresar nombres de usuario.
Si el usuario ya existe en el set:
Muestra "Usuario ya registrado".
Si no existe:
Agrégalo al set.
Muestra "Usuario registrado correctamente".
El programa debe terminar cuando el usuario escriba "salir".
"""
usuarios = set()
texto = input("Porfavor ingrese un nombre de usuario: ")
while texto != "salir":
    if texto in usuarios:
        print("Usuario ya registrado")
    else:
        usuarios.add(texto)
        print("Usuario registrado correctamente")
    texto = input("Porfavor ingrese un nombre de usuario: ")
print("Usuarios registrados:", usuarios)