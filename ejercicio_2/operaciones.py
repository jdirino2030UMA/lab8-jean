"""EJERCICIO 10 — Lógica del reporte

Implementa generar_reporte(productos). Cada producto tiene nombre único,
precio y stock enteros no negativos, y categoria.
Devuelve un diccionario con:
- disponibles: lista de nombres con stock > 0, en el orden original.
  Usa filter y map con lambda.
- valor_total: suma de precio * stock de todos los productos.
  Usa map y reduce con lambda, con valor inicial 0.
- hay_agotados: booleano que indica si algún stock es 0.
  Usa any sobre map con lambda.
- categorias: set con todas las categorías. Usa comprensión de sets.
- precios_con_recargo: lista de tuplas (nombre, precio con recargo del 10 %),
  solo para productos con stock > 0, en el orden original.
  Define una lambda para el recargo, redondeado a dos decimales con round,
  e invócala dentro de una comprensión de listas.
No modifiques productos ni imprimas dentro de la función.
Para [] devuelve listas y set vacíos, valor_total=0 y hay_agotados=False.
"""

from functools import reduce


def generar_reporte(productos):
    con_stock = filter(lambda p: p["stock"] > 0, productos)
    disponibles = list(map(lambda p: p["nombre"], con_stock))

    valores = map(lambda p: p["precio"] * p["stock"], productos)
    valor_total = reduce(lambda acumulado, v: acumulado + v, valores, 0)

    hay_agotados = any(map(lambda p: p["stock"] == 0, productos))

    categorias = {p["categoria"] for p in productos}

    recargo = lambda precio: round(precio * 1.1, 2)
    precios_con_recargo = [(p["nombre"], recargo(p["precio"]))
                           for p in productos if p["stock"] > 0]

    return {
        "disponibles": disponibles,
        "valor_total": valor_total,
        "hay_agotados": hay_agotados,
        "categorias": categorias,
        "precios_con_recargo": precios_con_recargo,
    }
