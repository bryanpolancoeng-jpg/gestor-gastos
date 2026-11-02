"""Lectura y escritura de los gastos en un archivo JSON."""
import json
from pathlib import Path

ARCHIVO_POR_DEFECTO = Path("gastos.json")


def cargar_gastos(ruta=ARCHIVO_POR_DEFECTO):
    """Devuelve la lista de gastos guardados (lista vacía si no hay archivo)."""
    ruta = Path(ruta)
    if not ruta.exists():
        return []
    try:
        with ruta.open("r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        # Archivo dañado: se empieza de cero para no romper el programa.
        return []


def guardar_gastos(gastos, ruta=ARCHIVO_POR_DEFECTO):
    """Guarda la lista de gastos en disco."""
    with Path(ruta).open("w", encoding="utf-8") as f:
        json.dump(gastos, f, ensure_ascii=False, indent=2)
