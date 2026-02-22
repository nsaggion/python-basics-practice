"""
Ejercicio de práctica en Python.
Tema: Varibales.
Nivel: Medio.
"""
"""
Enunciado:
Crea una variable global llamada mensaje con el valor:
- "Mensaje global"
Crea una función llamada mostrar() que:
Cree una variable local también llamada mensaje con el valor:
- "Mensaje local"
Imprima el valor de la variable dentro de la función.
Fuera de la función:
- Imprime el valor de mensaje antes de llamar a la función.
Llama a la función.
Imprime nuevamente el valor de mensaje.
"""
mensaje = "Mensaje global"
def mostrar():
    mensaje = "Mensaje local"
    print(mensaje)
print(mensaje)
mostrar()
print(mensaje)
