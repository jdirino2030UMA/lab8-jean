"""
Reservar y liberar puestos

DATOS
puestos = [[1, 0, 1], [0, 0, 1]]

IMPLEMENTA
1. reservar_puesto(puestos, coordenada): si la coordenada es valida y el puesto
   esta disponible, cambia su estado a 1 y devuelve True. En otro caso, False.
2. liberar_puesto(puestos, coordenada): si la coordenada es valida y el puesto
   esta ocupado, cambia su estado a 0 y devuelve True. En otro caso, False.
Rechaza indices negativos y coordenadas fuera del tablero.
Supone que coordenada es una tupla de dos enteros y el tablero es rectangular,
no vacio y contiene solo 0 y 1. Estas funciones SI modifican el tablero.

COMPROBACIONES CON PRINT
Realiza en orden, sobre el mismo tablero:
- Reservar (0, 1): True.
- Reservar otra vez (0, 1): False.
- Liberar (1, 2): True.
- Liberar otra vez (1, 2): False.
- Reservar (5, 0): False.
- Reservar (-1, 0): False.
Muestra el tablero final y agrega una comprobacion propia.

ANALISIS EN COMENTARIOS
Es necesario recorrer todo el tablero para reservar una coordenada conocida?
Justifica la complejidad de reservar, sin contar la impresion del tablero.

COMMIT SUGERIDO
Completa ejercicio 3: reservas y liberaciones
"""

def es_valida(puestos, coordenada):
    # el tablero es rectangular, asi que basta con el largo de la fila 0
    fila, columna = coordenada
    return 0 <= fila < len(puestos) and 0 <= columna < len(puestos[0])


def reservar_puesto(puestos, coordenada):
    if not es_valida(puestos, coordenada):
        return False
    fila, columna = coordenada
    if puestos[fila][columna] == 0:
        puestos[fila][columna] = 1
        return True
    return False


def liberar_puesto(puestos, coordenada):
    if not es_valida(puestos, coordenada):
        return False
    fila, columna = coordenada
    if puestos[fila][columna] == 1:
        puestos[fila][columna] = 0
        return True
    return False


if __name__ == "__main__":
    puestos = [[1, 0, 1], [0, 0, 1]]

    print("Reservar (0, 1):", reservar_puesto(puestos, (0, 1)))        # True
    print("Reservar (0, 1) otra vez:", reservar_puesto(puestos, (0, 1)))  # False
    print("Liberar (1, 2):", liberar_puesto(puestos, (1, 2)))          # True
    print("Liberar (1, 2) otra vez:", liberar_puesto(puestos, (1, 2)))  # False
    print("Reservar (5, 0):", reservar_puesto(puestos, (5, 0)))        # False
    print("Reservar (-1, 0):", reservar_puesto(puestos, (-1, 0)))      # False
    print("Tablero final:", puestos)  # [[1, 1, 1], [0, 0, 0]]

    # caso propio: columna fuera del tablero y liberar algo que ya estaba libre
    print("Reservar (0, 3):", reservar_puesto(puestos, (0, 3)))  # False
    print("Liberar (1, 0):", liberar_puesto(puestos, (1, 0)))    # False
    print("Reservar (1, 0):", reservar_puesto(puestos, (1, 0)))  # True
    print("Tablero:", puestos)  # [[1, 1, 1], [1, 0, 0]]

# ANALISIS
# No hace falta recorrer el tablero. Si ya sabemos la coordenada, se entra
# directo con puestos[fila][columna]. Lo unico que se hace es comparar la
# fila y la columna con len() y revisar/cambiar una sola celda, siempre la
# misma cantidad de pasos sin importar el tamano del tablero -> O(1).
