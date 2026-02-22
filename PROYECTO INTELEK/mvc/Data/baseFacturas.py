import os
import csv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVO = os.path.join(BASE_DIR, "csv", "facturas.csv")

def leerFacturas():
    try:
        if not os.path.exists(ARCHIVO): return []
        datos = []
        with open(ARCHIVO, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            for f in reader:
                if f: datos.append(f)
        return datos
    except Exception as e:
        print(f"Error leer facturas: {e}")
        return []

def guardarFactura(fila):
    try:
        # Estructura: [id_fac, id_cli, fecha, total, detalle, estado] [cite: 136]
        # Agregamos el estado inicial 'Completado'
        fila.append("Completado")
        with open(ARCHIVO, "a", newline="", encoding="utf-8") as file:
            csv.writer(file).writerow(fila)
        return True
    except Exception as e:
        print(f"Error guardar factura: {e}")
        return False

def cambiarEstadoFactura(idFac, nuevoEstado):
    try:
        facturas = leerFacturas()
        for f in facturas:
            if f[0] == str(idFac):
                f[-1] = nuevoEstado # El estado es la ultima columna
        with open(ARCHIVO, "w", newline="", encoding="utf-8") as file:
            csv.writer(file).writerows(facturas)
        return True
    except Exception as e:
        print(f"Error estado factura: {e}")
        return False