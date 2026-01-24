def menuReportes():
    print("\n--- REPORTES ---")
    print("1. Por Categoria")
    print("2. Bajo Stock")
    print("3. Historial")
    print("4. Volver")

def mostrarReporteCategoria(lista):
    print("\n--- REPORTE CATEGORIA ---")
    for item in lista:
        print(f"Cat: {item[2]} | {item[1]} | Stock: {item[4]}")

def mostrarReporteBajoStock(lista):
    print("\n--- BAJO STOCK ---")
    if not lista:
        print("No hay alertas.")
    for item in lista:
        print(f"ALERTA ID {item[0]}: {item[1]} (Stock: {item[4]})")

def mostrarHistorial(lista):
    print("\n--- HISTORIAL ---")
    for item in lista:
        print(f"{item[3]} | {item[1]} | Cant: {item[2]} (ID Prod: {item[0]})")