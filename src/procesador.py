import csv

class Analizador:
    def __init__(self, ruta_csv):
        self.ruta_csv = ruta_csv
        self.datos = self.leer_csv()

    def leer_csv(self):
        datos = []
        with open(self.ruta_csv, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo, delimiter='|')
            for fila in lector:
                if "PROVINCIA" in fila and "TOTAL_VENTAS" in fila:
                    datos.append(fila)
        return datos

    def ventas_totales_por_provincia(self):
        totales = {}
        for fila in self.datos:
            provincia = fila["PROVINCIA"].upper()
            try:
                total_venta = float(fila["TOTAL_VENTAS"])
            except ValueError:
                total_venta = 0.0
            totales[provincia] = totales.get(provincia, 0.0) + total_venta
        return totales

    def ventas_por_provincia(self, nombre):
        totales = self.ventas_totales_por_provincia()
        nombre_normalizado = nombre.upper()
        if nombre_normalizado not in totales:
            raise KeyError(f"La provincia '{nombre}' no existe en el dataset.")
        return totales[nombre_normalizado]