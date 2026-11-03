"""
Mapa de puestos

DATOS
puestos = [[1, 0, 1], [0, 0, 1]]
0: disponible. 1: ocupado. Las coordenadas son tuplas (fila, columna), desde cero.

IMPLEMENTA
1. crear_mapa(puestos): devuelve un diccionario {(fila, columna): estado}.
   Utiliza una comprension de diccionarios.
2. obtener_disponibles(puestos): devuelve un set de coordenadas disponibles.
   Utiliza una comprension de conjuntos.
No modifiques el tablero.

COMPROBACIONES CON PRINT
- Muestra el mapa completo y los disponibles.
- Consulta el estado de (1, 2) en el mapa: debe ser 1.
- Disponibles esperados: {(0, 1), (1, 0), (1, 1)}. El orden no importa.
- Agrega y comprueba otro tablero propio.

ANALISIS EN COMENTARIOS
- Cuantas celdas se revisan al obtener los disponibles en el ejemplo?
- Cuantas se revisan para f filas y c columnas? Y para n filas y n columnas?

COMMIT SUGERIDO
Completa ejercicio 1: mapa y puestos disponibles
"""

def crear_mapa(puestos):
    # clave = (fila, columna), valor = el 0 o el 1 de esa celda
    return {(i, j): puestos[i][j]
            for i in range(len(puestos))
            for j in range(len(puestos[i]))}


def obtener_disponibles(puestos):
    # solo las coordenadas donde hay un 0
    return {(i, j)
            for i in range(len(puestos))
            for j in range(len(puestos[i]))
            if puestos[i][j] == 0}


if __name__ == "__main__":
    puestos = [[1, 0, 1], [0, 0, 1]]

    mapa = crear_mapa(puestos)
    print("Mapa:", mapa)
    print("Disponibles:", obtener_disponibles(puestos))
    print("Estado de (1, 2):", mapa[(1, 2)])  # 1
    print("Tablero sin cambios:", puestos)

    # caso propio: 3x2, todo ocupado menos dos puestos
    otro = [[1, 1], [0, 1], [1, 0]]
    print("Mapa propio:", crear_mapa(otro))
    print("Disponibles propio:", obtener_disponibles(otro))  # {(1, 0), (2, 1)}

# ANALISIS
# - En el ejemplo se revisan las 6 celdas (2 filas x 3 columnas), hay que
#   mirar todas para saber cuales son 0.
# - Con f filas y c columnas se revisan f * c celdas -> O(f*c).
#   Si son n filas y n columnas: n * n = n^2 celdas -> O(n^2).
