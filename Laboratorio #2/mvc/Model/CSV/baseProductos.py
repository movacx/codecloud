import sys

import os

sys.stdout.reconfigure(encoding="utf-8")

import csv

BASE_DIR = os.path.dirname(__file__)

ARCHIVO = os.path.join(BASE_DIR, 'csv', 'productos.csv')

#'csv/productos.csv'

def guardarProductos(codigoUnico, nombre, categoria, precio, stock):
    #open    (src, atributos, lectura, systemaenco)
    with open(ARCHIVO, "a", newline="", encoding="utf-8") as archivoparaguardar:
              writer = csv.writer(archivoparaguardar)
              
              writer.writerow([codigoUnico, nombre, categoria, precio, stock])
              
              print("Se guardaron datos")
              
 
 
def mostrarProductos():
    with open(ARCHIVO, "r", newline="", encoding="utf-8") as archivoparaleer:
        reader = csv.reader(archivoparaleer)
        
        for item in reader:
            print(item)
            
def mostrarProductoId(codigoUnico):
    with open(ARCHIVO, "r", newline="", encoding="utf-8") as archivoparaleer:
        reader = csv.reader(archivoparaleer)
        
        for item in reader:
            if item[0] == str(id):
                return item           


def modificarProducto(codigoUnico, nombre, categoria, precio, stock):
   # print(codigoUnico, nombre, categoria, precio, stock)
    arregloVacio = []
    
    with open(ARCHIVO, "r", newline="", encoding="utf-8") as archivoparaleer:
        reader = csv.reader(archivoparaleer)
        
        for item in reader:
            if item[0] == str(id):
                item[1] = nombre
                item[2] = edad
                
            arregloVacio.append(item)
            
    with open(ARCHIVO, "w", newline="", encoding="utf-8") as archivoparaescribir:
        writer = csv.writer(archivoparaescribir)
        writer.writerows(arregloVacio)
  
    print("actualizo el producto")   
    #print(arregloVacio)



def eliminarProductos(id):
   # print(id, nombre, edad)
    arregloVacio = []
    
    with open(ARCHIVO, "r", newline="", encoding="utf-8") as archivoparaleer:
        reader = csv.reader(archivoparaleer)
        
        for item in reader:
            if item[0] != str(id):                               
                arregloVacio.append(item)
            
    with open(ARCHIVO, "w", newline="", encoding="utf-8") as archivoparaescribir:
        writer = csv.writer(archivoparaescribir)
        writer.writerows(arregloVacio)
  
    print("Elimino el producto")   
    #print(arregloVacio)

print(mostrarProductoId((3))
#guar(3, "Isaac", 21)
modificarProductos(3, "Alberto", 11)
print(mostrarProductoId(3))
eliminarProductos((2)
mostrarProductos()
