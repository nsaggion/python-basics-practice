"""
Ejercicio de práctica en Python.
Tema: Funciones.
Nivel: Medio.
"""
"""
Enunciado:
Pida al usuario que ingrese un número.
Intente convertirlo a entero.
Después intente dividir 100 entre ese número.
Si ocurre cualquier error, debe:
Mostrar el mensaje:
- Ocurrió un error:
Mostrar también el error real que generó Python.
Finalmente, mostrar:
- Programa finalizado.
"""
try:
    num = input("Ingrese un número: ")
    num = int(num)
    total = 100 / num
except Exception as e:
    print("Ocurrió un error:",e)
else:
    print(f"El numero {num} dividido 100 a dado como resultado: {total}")
finally:
    print("Programa finalizado.")