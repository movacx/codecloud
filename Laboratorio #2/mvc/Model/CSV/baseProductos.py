import sys

import os

import csv

sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = os.path.dirname(__file__)

FOLDER = os.path.join(BASE_DIR, 'csv')

ARCHIVO = os.path.join(FOLDER, 'productos.csv')

def guardarProducto(codigoUnico, nombre, categoria, precio, stock):
    
    with open(ARCHIVO, "a", newline="", encoding="utf-8") as archivoparaguardar:
        
        writer = csv.writer(archivoparaguardar)
        writer.writerow([codigoUnico, nombre, categoria, precio, stock])
        
        print(f"Producto {nombre} guardado exitosamente.")

def mostrarProductos():
    
    with open(ARCHIVO, "r", newline="", encoding="utf-8") as archivoparaleer:
        
        reader = csv.reader(archivoparaleer)
        
        for item in reader:
            print(item)

def mostrarProductoId(codigoUnico):
    
    with open(ARCHIVO, "r", newline="", encoding="utf-8") as archivoparaleer:
        
        reader = csv.reader(archivoparaleer)
       
        for item in reader:
            if item[0] == str(codigoUnico):
                return item
        return "No encontrado"

def modificarProducto(codigoUnico, nombre, categoria, precio, stock):
    arregloVacio = []
    encontrado = False
    
    with open(ARCHIVO, "r", newline="", encoding="utf-8") as archivoparaleer:
        
        reader = csv.reader(archivoparaleer)
        
        for item in reader:
            if item[0] == str(codigoUnico):
                
                item = [codigoUnico, nombre, categoria, precio, stock]
                encontrado = True
            arregloVacio.append(item)
            
    if encontrado:
        with open(ARCHIVO, "w", newline="", encoding="utf-8") as archivoparaescribir:
            
            writer = csv.writer(archivoparaescribir)
            writer.writerows(arregloVacio)
        
        print(f"Producto {codigoUnico} actualizado.")
    else:
        print("Producto no encontrado para modificar.")

def eliminarProductos(codigoUnico):
    arregloVacio = []

    with open(ARCHIVO, "r", newline="", encoding="utf-8") as archivoparaleer:
        
        reader = csv.reader(archivoparaleer)
        
        for item in reader:
            if item[0] != str(codigoUnico):                                
                arregloVacio.append(item)
            
    with open(ARCHIVO, "w", newline="", encoding="utf-8") as archivoparaescribir:
        
        writer = csv.writer(archivoparaescribir)
        writer.writerows(arregloVacio)
    
    print(f"Eliminado el producto: {codigoUnico}")


guardarProducto(2, "sonido", "Peri", 250, 10)
guardarProducto(3, "compu", "Peri", 100, 20)


print("Buscando  3:", mostrarProductoId(3))


modificarProducto(3, "compu", "Peri", 400, 5)


eliminarProductos(2)


print("Lista final:")
mostrarProductos()
