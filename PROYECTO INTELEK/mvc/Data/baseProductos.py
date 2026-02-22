import os
import csv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVO = os.path.join(BASE_DIR, "csv", "productos.csv")

def listarProductos():
    try:
        if not os.path.exists(ARCHIVO): return []
        lista = []
        with open(ARCHIVO, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            for item in reader:
                if item: lista.append(item)
        return lista
    except Exception as e:
        print(f"Error listar productos: {e}")
        return []

def guardarProducto(objPro):
    try:
        # Lógica de autoincremento para ID [cite: 120]
        idNuevo = 1
        actuales = listarProductos()
        if actuales:
            idNuevo = int(actuales[-1][0]) + 1
        objPro.ide = idNuevo

        with open(ARCHIVO, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(objPro.importarToCsv())
        return True
    except Exception as e:
        print(f"Error guardar producto: {e}")
        return False

def eliminarProducto(idPro):
    try:
        productos = listarProductos()
        nuevoArreglo = [p for p in productos if p[0] != str(idPro)]
        with open(ARCHIVO, "w", newline="", encoding="utf-8") as file:
            csv.writer(file).writerows(nuevoArreglo)
        return True
    except Exception as e:
        print(f"Error eliminar: {e}")
        return False

def restarStock(idPro, cantidad):
    try:
        productos = listarProductos()
        for p in productos:
            if p[0] == str(idPro):
                p[4] = str(int(p[4]) - cantidad)
        with open(ARCHIVO, "w", newline="", encoding="utf-8") as file:
            csv.writer(file).writerows(productos)
        return True
    except Exception as e:
        print(f"Error stock: {e}")
        return False