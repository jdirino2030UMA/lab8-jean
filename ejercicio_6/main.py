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
    resumen = {}
    for nombre in laboratorios:
        tablero = laboratorios[nombre]
        total = sum([len(fila) for fila in tablero])
        ocupados = sum([sum(fila) for fila in tablero])
        resumen[nombre] = (total, ocupados, total - ocupados)
    return resumen


def laboratorios_con_cupo(resumen, cantidad):
    if cantidad <= 0:
        return set()
    # posicion 2 de la tupla = disponibles
    return {nombre for nombre in resumen if resumen[nombre][2] >= cantidad}


if __name__ == "__main__":
    laboratorios = {
        "A": [[1, 0, 0], [0, 1, 0]],
        "B": [[1, 1], [1, 1]],
        "C": [[0, 0, 0]]
    }

    resumen = resumir_laboratorios(laboratorios)
    print("Resumen:", resumen)  # {'A': (6, 2, 4), 'B': (4, 4, 0), 'C': (3, 0, 3)}
    print("Cupo 3:", laboratorios_con_cupo(resumen, 3))  # {'A', 'C'}
    print("Cupo 4:", laboratorios_con_cupo(resumen, 4))  # {'A'}
    print("Cupo 5:", laboratorios_con_cupo(resumen, 5))  # set()
    print("Cupo 0:", laboratorios_con_cupo(resumen, 0))  # set()

    # caso propio: agrego el D
    laboratorios["D"] = [[0, 0], [0, 0], [0, 1]]
    resumen = resumir_laboratorios(laboratorios)
    print("Resumen con D:", resumen)  # ... 'D': (6, 1, 5)
    print("Cupo 3:", laboratorios_con_cupo(resumen, 3))  # {'A', 'C', 'D'}
    print("Cupo 4:", laboratorios_con_cupo(resumen, 4))  # {'A', 'D'}
    print("Cupo 5:", laboratorios_con_cupo(resumen, 5))  # {'D'}
    print("Cupo 0:", laboratorios_con_cupo(resumen, 0))  # set()

# ANALISIS
# resumir_laboratorios: revisa todos los puestos de todos los laboratorios
# (sum y len recorren cada fila). Cada puesto se mira una cantidad fija de
# veces, asi que el trabajo crece con el total de puestos -> O(P).
# laboratorios_con_cupo: no toca los tableros, solo revisa una tupla del
# resumen por laboratorio y saca la posicion 2, que es O(1). Son L
# laboratorios -> O(L).
