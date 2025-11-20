from src.procesador import Analizador

def main():
    archivo = "datos/sri_ventas_2024.csv"
    analizador = Analizador(archivo)

    print("Ventas totales por provincia:")
    resumen = analizador.ventas_totales_por_provincia()
    for prov, total in resumen.items():
        print(f"\t{prov}: ${total:.2f}")

    print("\nConsulta de ventas por provincia:")
    provincia = input("\tIngrese el nombre de una provincia: ")
    try:
        ventas = analizador.ventas_por_provincia(provincia)
        print(f"\tVentas de {provincia}: ${ventas:,.2f}")
    except KeyError:
        print(f"\tLa provincia '{provincia}' no existe en el archivo.")

if __name__ == "__main__":
    main()