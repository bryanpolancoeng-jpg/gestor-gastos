import unittest

from gastos.logica import (agregar_gasto, eliminar_gasto,
                           resumen_por_categoria, total_gastado)


class PruebasGastos(unittest.TestCase):
    def setUp(self):
        self.gastos = []
        agregar_gasto(self.gastos, "Almuerzo", 5.50, "comida", "2026-11-01")
        agregar_gasto(self.gastos, "Bus", 1.25, "transporte", "2026-11-01")
        agregar_gasto(self.gastos, "Cena", 8.00, "comida", "2026-11-02")

    def test_agregar_asigna_id_y_categoria(self):
        self.assertEqual(self.gastos[-1]["id"], 3)
        self.assertEqual(self.gastos[0]["categoria"], "Comida")

    def test_monto_invalido(self):
        with self.assertRaises(ValueError):
            agregar_gasto(self.gastos, "Algo", -5, "otros")

    def test_descripcion_vacia(self):
        with self.assertRaises(ValueError):
            agregar_gasto(self.gastos, "  ", 5, "otros")

    def test_eliminar(self):
        self.assertTrue(eliminar_gasto(self.gastos, 2))
        self.assertFalse(eliminar_gasto(self.gastos, 99))
        self.assertEqual(len(self.gastos), 2)

    def test_total_y_resumen(self):
        self.assertEqual(total_gastado(self.gastos), 14.75)
        self.assertEqual(resumen_por_categoria(self.gastos),
                         {"Comida": 13.5, "Transporte": 1.25})


if __name__ == "__main__":
    unittest.main()
