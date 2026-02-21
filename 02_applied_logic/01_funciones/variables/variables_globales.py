"""
Ejercicio de práctica en Python.
Tema: Funciones.
Nivel: Medio.
"""
"""
Enunciado:
Crea una variable global llamada contador y asígnale el valor 0.
Después:
- Crea una función llamada incrementar().
- Dentro de la función, aumenta el valor de contador en 1.
- Muestra el valor actualizado de contador.
- Llama a la función tres veces.
Finalmente, imprime el valor final de contador fuera de la función.
"""
contador = 0
def incremental ():
    global contador
    contador+=1
for i in range (3):
    incremental()
print("Valor final del contador:", contador)