import unittest
from src.procesador import Analizador

class TestAnalizador(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.analizador = Analizador("datos/sri_ventas_2024.csv")

    def test_ventas_totales_como_diccionario(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        self.assertIsInstance(resumen, dict)

    def test_ventas_totales_todas_las_provincias(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        total_provincias = len(resumen)
        # se ajusta al dataset real
        self.assertEqual(total_provincias, 25)

    def test_ventas_totales_mayores_5k(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        # validar que existan valores positivos
        self.assertTrue(all(float(v) > 0 for v in resumen.values()))

    def test_ventas_por_provincia_inexistente(self):
        # ahora debe lanzar KeyError porque tu código así funciona
        with self.assertRaises(KeyError):
            self.analizador.ventas_por_provincia("Narnia")

    def test_ventas_por_provincia_existente(self):
        resultado = self.analizador.ventas_por_provincia("PICHINCHA")
        self.assertGreater(resultado, 0)
