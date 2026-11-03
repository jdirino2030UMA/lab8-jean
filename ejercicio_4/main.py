"""
Reporte de ocupacion

DATOS
puestos = [[1, 0, 1, 0], [0, 0, 1, 0], [1, 1, 1, 0]]

IMPLEMENTA
1. resumir_filas(puestos): devuelve una lista de tuplas
   (numero_de_fila, ocupados, disponibles). Puedes utilizar sum().
2. transformar_estados(puestos, transformar): aplica la funcion recibida a cada
   estado mediante una comprension anidada. Devuelve una tabla nueva sin
   modificar el tablero original.
Llama a transformar_estados con una lambda que transforme 0 en "Disponible"
y 1 en "Ocupado".

COMPROBACIONES CON PRINT
- Resumen esperado: [(0, 2, 2), (1, 1, 3), (2, 3, 1)].
- Muestra la tabla de textos y el tablero original despues de transformarlo.
- Agrega un tablero propio con una unica fila y comprueba sus resultados.

ANALISIS EN COMENTARIOS
- Es correcto decir que una comprension evita recorrer los puestos? Explica.
- Cuantos estados se transforman en el ejemplo inicial?

COMMIT SUGERIDO
Completa ejercicio 4: reportes y transformacion de estados
"""

def resumir_filas(puestos):
    # como los ocupados son 1, sum(fila) da justo los ocupados
    return [(i, sum(puestos[i]), len(puestos[i]) - sum(puestos[i]))
            for i in range(len(puestos))]


def transformar_estados(puestos, transformar):
    # tabla nueva, se conservan las filas
    return [[transformar(estado) for estado in fila] for fila in puestos]


if __name__ == "__main__":
    puestos = [[1, 0, 1, 0], [0, 0, 1, 0], [1, 1, 1, 0]]

    print("Resumen:", resumir_filas(puestos))  # [(0, 2, 2), (1, 1, 3), (2, 3, 1)]

    a_texto = lambda estado: "Disponible" if estado == 0 else "Ocupado"
    textos = transformar_estados(puestos, a_texto)
    print("Textos:", textos)
    print("Original:", puestos)  # sigue igual

    # caso propio: una sola fila
    una_fila = [[0, 1, 1, 0, 1]]
    print("Resumen propio:", resumir_filas(una_fila))  # [(0, 3, 2)]
    print("Textos propio:", transformar_estados(una_fila, a_texto))
    # [['Disponible', 'Ocupado', 'Ocupado', 'Disponible', 'Ocupado']]
    print("Original propio:", una_fila)

# ANALISIS
# - No. La comprension se escribe mas corto, pero por dentro igual recorre
#   cada puesto uno por uno, como los dos for anidados. Cambia la forma de
#   escribirlo, no el trabajo que se hace.
# - Se transforman 12 estados (3 filas x 4 columnas), la lambda se llama
#   12 veces.
