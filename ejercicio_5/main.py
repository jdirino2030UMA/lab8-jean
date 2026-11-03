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
    if len(coordenadas) == 0:
        return False

    # si al pasarlo a set se pierden elementos, habia repetidos
    if len(set(coordenadas)) != len(coordenadas):
        return False

    # primero se revisa todo, sin tocar nada
    for fila, columna in coordenadas:
        if fila < 0 or fila >= len(puestos):
            return False
        if columna < 0 or columna >= len(puestos[0]):
            return False
        if puestos[fila][columna] == 1:
            return False

    # si llego aqui, todo esta bien y ya se puede reservar
    for fila, columna in coordenadas:
        puestos[fila][columna] = 1
    return True


if __name__ == "__main__":
    puestos = [[1, 0, 0], [0, 1, 0]]

    casos = [
        [(0, 1), (1, 0)],   # True
        [(0, 1), (0, 1)],   # False, repetida
        [(0, 1), (0, 0)],   # False, (0, 0) ocupado
        [(0, 1), (8, 0)],   # False, fila 8 no existe
        [],                 # False, vacia
        [(0, 2), (1, 2)],   # propio: True, la columna 2 esta libre
        [(1, 2), (-1, 0)],  # propio: False, negativo y no cambia (1, 2)
    ]

    for grupo in casos:
        tablero = [[estado for estado in fila] for fila in puestos]  # copia nueva
        print(grupo, "->", reservar_grupo(tablero, grupo), tablero)

# ANALISIS
# Porque si se reserva cada uno apenas se revisa y despues aparece uno malo
# (ocupado, fuera del tablero o repetido), la funcion devuelve False pero los
# primeros ya quedaron en 1. El tablero quedaria a medias, con puestos
# reservados de un grupo que no se pudo reservar. Por eso primero se revisa
# todo el grupo y solo al final se cambia.
