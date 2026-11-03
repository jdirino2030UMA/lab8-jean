"""
Reto: varios laboratorios

DATOS
laboratorios = {
    "A": [[1, 0, 0], [0, 1, 0]],
    "B": [[1, 1], [1, 1]],
    "C": [[0, 0, 0]]
}

IMPLEMENTA
1. resumir_laboratorios(laboratorios): devuelve un diccionario con cada nombre
   como clave y una tupla (total_de_puestos, ocupados, disponibles) como valor.
2. laboratorios_con_cupo(resumen, cantidad): devuelve un set con los nombres
   de los laboratorios con al menos cantidad puestos disponibles.
   Si cantidad <= 0, devuelve un set vacio.
No modifiques los datos recibidos. Puedes utilizar sum().

COMPROBACIONES CON PRINT
- Resumen esperado: {"A": (6, 2, 4), "B": (4, 4, 0), "C": (3, 0, 3)}.
- Para cantidad 3: {"A", "C"}.
- Para cantidad 4: {"A"}.
- Para cantidad 5: set vacio.
- Comprueba tambien cantidad 0.
- Agrega un laboratorio propio y repite las consultas.
El orden de los elementos de un set no importa.

ANALISIS EN COMENTARIOS
Usa P para el total de puestos y L para el numero de laboratorios.
Que elementos revisa cada funcion? Justifica sus complejidades por separado.

COMMIT SUGERIDO
Completa ejercicio 6: resumen de multiples laboratorios
"""

def resumir_laboratorios(laboratorios):
    # TODO: implementa esta funcion.
    pass


def laboratorios_con_cupo(resumen, cantidad):
    # TODO: implementa esta funcion.
    pass


if __name__ == "__main__":
    laboratorios = {
        "A": [[1, 0, 0], [0, 1, 0]],
        "B": [[1, 1], [1, 1]],
        "C": [[0, 0, 0]]
    }

    # TODO: escribe las llamadas y muestra los resultados con print.
    # TODO: agrega al menos un caso propio.

# ANALISIS
# TODO: responde aqui las preguntas del enunciado.
