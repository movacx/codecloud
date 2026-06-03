def menuReportes():
    print("\nReportes")
    print("1. Por Categoria")
    print("2. Bajo Stock")
    print("3. Historial")
    print("4. Volver")

def mostrarReporteCategoria(lista):
    print("\nReporte por Categoria")
    for item in lista:
        print(f"Catidad: {item[2]} | {item[1]} | Stock: {item[4]}")

def mostrarReporteBajoStock(lista):
    print("\nBajos de Stock")
    if not lista:
        print("No hay alertas.")
    for item in lista:
        print(f"Alerta id {item[0]}: {item[1]} (Stock: {item[4]})")

def mostrarHistorial(lista):
    print("\nHistorial")
    for item in lista:
        print(f"{item[3]} | {item[1]} | Cantidad: {item[2]} (Id Productos: {item[0]})")