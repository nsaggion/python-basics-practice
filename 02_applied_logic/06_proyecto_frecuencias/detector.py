"""
PROYECTO: Detector de Frecuencias (Simulado)
OBJETIVO: Aplicar lógica de programación para clasificar frecuencias de audio 
y gestionar la persistencia de datos en archivos externos.

REQUERIMIENTOS:
1. Procesar una lista de frecuencias en hercios (Hz).
2. Implementar una función que clasifique cada frecuencia en:
    - NOTA: Si está dentro de un rango de tolerancia (±0.5 Hz).
    - RUIDO: Si el volumen es demasiado bajo (opcional).
    - DESCONOCIDO: Si no coincide con ninguna nota programada.
3. Guardar el historial de detecciones en un archivo .txt sin borrar lo anterior.
4. Manejar posibles errores (como datos no numéricos).
"""
# Lista de frecuencias capturadas (Simulación)
frecuencias_capturadas = [440.0, 261.63, 329.63, 440.5, 500.0]

def identificar_nota(hz):
    """
    Traduce Hz a Notas.
    Aproximaciones:
    - 261.63 -> DO
    - 329.63 -> MI
    - 440.0  -> LA
    """
    # ESCRIBE AQUÍ TU LÓGICA (Usa if/elif/else)
    # Si no es ninguna de esas, que devuelva "Desconocido"
    pass

# TAREA: 
# 1. Recorre la lista de frecuencias.
# 2. Llama a la función para cada una.
# 3. Guarda el resultado en un archivo llamado 'registro_notas.txt'
#    Formato esperado: "Frecuencia: 440.0 - Nota: LA"