import sys
import os

sys.stdout.reconfigure(encoding = "utf-8")

import csv

BASE_DIR = os.path.dirname(__file__)
ARCHIVO = os.path.join(BASE_DIR, "CSV", "productos.csv")

#Metodo guardar Producto
def guardarProducto(id, nombre, categoria, precio, stock):
    # Aseguramos que se crea la carpeta si no existe (opcional pero util)
    os.makedirs(os.path.dirname(ARCHIVO), exist_ok=True)
    
    with open(ARCHIVO, "a", newline="", encoding= "utf-8") as archivoParaGuardar:
        writer = csv.writer(archivoParaGuardar)
        writer.writerow([id, nombre, categoria, precio, stock])
        
    print ("Se guardaron los productos")
    
#Listar productos (Retornamos la lista para que el reporte la use tambien)
def listarProductos():
    listaDeItems = []
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding= "utf-8") as archivoparaleer:
            reader = csv.reader(archivoparaleer)
            for item in reader:
                print(item) # Imprime como pediste
                listaDeItems.append(item)
    return listaDeItems # Retornamos para usar en reportes

#Buscar por ID
def buscarProductoId(id):
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding = "utf-8") as archivoParaleer:
            reader = csv.reader(archivoParaleer)
        
            for item in reader:
                if item[0] == str(id):
                    return item
    return None
            
#Modificar Producto
def modificarProducto(id, nombre, categoria, precio, stock):
    arregloVacio = []
    encontrado = False
    
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", newline="", encoding="utf-8") as archivoParaLeer:
            reader = csv.reader(archivoParaLeer)
            for item in reader:
                if item[0] == str(id):
                    item[1] = nombre
                    item[2] = categoria
                    item[3] = precio
                    item[4] = stock
                    encontrado = True
                # IMPORTANTE: El append va DENTRO del for
                arregloVacio.append(item)
            
        with open(ARCHIVO, "w", newline="", encoding= "utf-8") as archivoParaEscribir:
            writer = csv.writer(archivoParaEscribir)
            # IMPORTANTE: Es writerows (plural)
            writer.writerows(arregloVacio) 
            
    return encontrado            

#Eliminar producto
def eliminarProductos(id):
    arregloVacio = [] #Datos temporales
    
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", newline="", encoding="utf-8") as archivoParaLeer:
            reader = csv.reader(archivoParaLeer)
            
            for item in reader:
                if item[0] != str(id):                               
                    arregloVacio.append(item)
                
        with open(ARCHIVO, "w", newline="", encoding="utf-8") as archivoParaEscribir:
            writer = csv.writer(archivoParaEscribir)
            writer.writerows(arregloVacio)

    print("Elimino el producto")