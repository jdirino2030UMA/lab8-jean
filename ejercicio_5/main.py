"""
Reto: reservas de grupos

DATOS
puestos = [[1, 0, 0], [0, 1, 0]]

IMPLEMENTA
reservar_grupo(puestos, coordenadas): recibe una lista de tuplas (fila, columna).
Supone que cada coordenada es una tupla de dos enteros y que el tablero es
rectangular, no vacio, con estados 0 o 1.
- Si la lista esta vacia, devuelve False.
- Si hay coordenadas repetidas, invalidas, negativas o puestos ocupados,
  devuelve False y NO modifica ninguna celda.
- Solo si todas las coordenadas son validas y disponibles, reserva todos los
  puestos (estado 1) y devuelve True.
Utiliza un set para detectar duplicados. Comprueba todas las condiciones
antes de modificar el tablero. No utilices input().

COMPROBACIONES CON PRINT
Usa una copia NUEVA del tablero inicial para CADA caso:
- [(0, 1), (1, 0)]: True.
- [(0, 1), (0, 1)]: False.
- [(0, 1), (0, 0)]: False.
- [(0, 1), (8, 0)]: False.
- []: False.
Muestra el tablero tras cada llamada. Agrega un caso propio.

ANALISIS EN COMENTARIOS
Por que no debes reservar cada puesto inmediatamente despues de comprobarlo,
antes de revisar el resto del grupo?

COMMIT SUGERIDO
Completa ejercicio 5: reserva de grupos sin cambios parciales
"""

def reservar_grupo(puestos, coordenadas):
    # TODO: implementa esta funcion.
    pass


if __name__ == "__main__":
    puestos = [[1, 0, 0], [0, 1, 0]]

    # TODO: escribe las llamadas y muestra los resultados con print.
    # TODO: agrega al menos un caso propio.

# ANALISIS
# TODO: responde aqui las preguntas del enunciado.
