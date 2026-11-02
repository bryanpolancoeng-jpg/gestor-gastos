"""Reglas de negocio: agregar, eliminar y resumir gastos."""
from datetime import date


def agregar_gasto(gastos, descripcion, monto, categoria, fecha=None):
    """Agrega un gasto validando los datos. Devuelve el gasto creado."""
    descripcion = descripcion.strip()
    categoria = categoria.strip().capitalize()
    if not descripcion:
        raise ValueError("La descripción no puede estar vacía.")
    if not categoria:
        raise ValueError("La categoría no puede estar vacía.")
    if monto <= 0:
        raise ValueError("El monto debe ser mayor que cero.")

    nuevo_id = max((g["id"] for g in gastos), default=0) + 1
    gasto = {
        "id": nuevo_id,
        "fecha": fecha or date.today().isoformat(),
        "descripcion": descripcion,
        "categoria": categoria,
        "monto": round(monto, 2),
    }
    gastos.append(gasto)
    return gasto


def eliminar_gasto(gastos, id_gasto):
    """Elimina el gasto con ese id. Devuelve True si existía."""
    for gasto in gastos:
        if gasto["id"] == id_gasto:
            gastos.remove(gasto)
            return True
    return False


def total_gastado(gastos):
    """Suma de todos los montos."""
    return round(sum(g["monto"] for g in gastos), 2)


def resumen_por_categoria(gastos):
    """Diccionario {categoria: total}, ordenado de mayor a menor."""
    totales = {}
    for g in gastos:
        totales[g["categoria"]] = totales.get(g["categoria"], 0) + g["monto"]
    ordenado = sorted(totales.items(), key=lambda par: par[1], reverse=True)
    return {cat: round(total, 2) for cat, total in ordenado}
