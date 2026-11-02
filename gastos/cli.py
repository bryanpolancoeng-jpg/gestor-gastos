"""Menú interactivo en consola."""
from .almacenamiento import cargar_gastos, guardar_gastos
from .logica import (agregar_gasto, eliminar_gasto, resumen_por_categoria,
                     total_gastado)

MENU = """
=== GESTOR DE GASTOS PERSONALES ===
1. Agregar gasto
2. Listar gastos
3. Eliminar gasto
4. Resumen por categoría
5. Salir
"""


def pedir_monto():
    """Pide un monto hasta que el usuario escriba un número válido."""
    while True:
        try:
            return float(input("Monto ($): ").replace(",", "."))
        except ValueError:
            print("  Ingresa un número válido (ejemplo: 12.50).")


def mostrar_gastos(gastos):
    if not gastos:
        print("\nNo hay gastos registrados.")
        return
    print(f"\n{'ID':<4}{'Fecha':<12}{'Categoría':<14}{'Descripción':<24}{'Monto':>10}")
    print("-" * 64)
    for g in gastos:
        print(f"{g['id']:<4}{g['fecha']:<12}{g['categoria']:<14}"
              f"{g['descripcion'][:22]:<24}{g['monto']:>10.2f}")
    print("-" * 64)
    print(f"{'TOTAL':<54}{total_gastado(gastos):>10.2f}")


def opcion_agregar(gastos):
    descripcion = input("Descripción: ")
    categoria = input("Categoría (Comida, Transporte, ...): ")
    monto = pedir_monto()
    try:
        gasto = agregar_gasto(gastos, descripcion, monto, categoria)
    except ValueError as error:
        print(f"  Error: {error}")
        return
    guardar_gastos(gastos)
    print(f"  Gasto #{gasto['id']} guardado.")


def opcion_eliminar(gastos):
    mostrar_gastos(gastos)
    if not gastos:
        return
    try:
        id_gasto = int(input("\nID del gasto a eliminar: "))
    except ValueError:
        print("  El ID debe ser un número entero.")
        return
    if eliminar_gasto(gastos, id_gasto):
        guardar_gastos(gastos)
        print("  Gasto eliminado.")
    else:
        print("  No existe un gasto con ese ID.")


def opcion_resumen(gastos):
    if not gastos:
        print("\nNo hay gastos registrados.")
        return
    print("\nResumen por categoría")
    print("-" * 30)
    for categoria, total in resumen_por_categoria(gastos).items():
        print(f"{categoria:<18}{total:>10.2f}")
    print("-" * 30)
    print(f"{'TOTAL':<18}{total_gastado(gastos):>10.2f}")


def main():
    gastos = cargar_gastos()
    while True:
        print(MENU)
        opcion = input("Elige una opción: ").strip()
        if opcion == "1":
            opcion_agregar(gastos)
        elif opcion == "2":
            mostrar_gastos(gastos)
        elif opcion == "3":
            opcion_eliminar(gastos)
        elif opcion == "4":
            opcion_resumen(gastos)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("  Opción no válida.")
