import os
import csv

dirData = os.path.dirname(os.path.abspath(__file__))
ARCHIVO = os.path.join(dirData, "csv", "productos.csv")

def listarProductos():
    try:
        if not os.path.exists(ARCHIVO): return []
        lista = []
        with open(ARCHIVO, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            for items in reader:
                if items: 
                    lista.append(items)
        return lista
    except Exception as e:
        print(f"Error listar productos: {e}")
        return []

def guardarProducto(objPro):
    try:
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
        nuevoArreglo = []
        for items in productos:
            if items:
                if items[0] != str(idPro):
                    nuevoArreglo.append(items)
                    
        with open(ARCHIVO, "w", newline="", encoding="utf-8") as file:
            csv.writer(file).writerows(nuevoArreglo)
        return True
    except Exception as e:
        print(f"Error eliminar: {e}")
        return False

def restarStock(idPro, cantidad):
    try:
        productos = listarProductos()
        for items in productos:
            if items:
                if items[0] == str(idPro):
                    items[4] = str(int(items[4]) - cantidad)
        with open(ARCHIVO, "w", newline="", encoding="utf-8") as file:
            csv.writer(file).writerows(productos)
        return True
    except Exception as e:
        print(f"Error stock: {e}")
        return False