"""
Ejercicio de práctica en Python.
Tema: Importación.
Nivel: Medio.
"""
"""
Enunciado:
Crea dos archivo:
- Operaciones.py
- main.py
En operaciones crea modulos con operaciones basicas y implmenta "if__name__=="__main__":".
En main importa esos modulos.
"""
import operaciones

print("Usando el módulo operaciones\n")

resultado1 = operaciones.sumar(8, 4)
resultado2 = operaciones.multiplicar(3, 6)

print("Resultado suma:", resultado1)
print("Resultado multiplicación:", resultado2)