import sys
import os

sys.stdout.reconfigure(encoding = "utf-8")

import csv

BASE_DIR = os.path.dirname(__file__)
ARCHIVO = os.path.join(BASE_DIR, "CSV", "productos.csv")

#Metodo guardar Producto
def guardarProducto(id, nombre, categoria, precio, stock):
	
	with open(ARCHIVO, "a", newline="", encoding= "utf-8") as archivoParaGuardar:
		writer = csv.writer(archivoParaGuardar)
		
	print ("Se guardaron los productos")
	
	
#Listar productos
def listarProductos():
	with open(ARCHIVO, "r", enconding= "utf-8") as archivoparaleer:
		reader = csv.reader(archivoparaleer)
		for item in reader:
			print(item)
	
#Buscar por ID
def buscarProductoId(id):
	with open(ARCHIVO, "r", encoding = "utf-8") as archivoparaleer:
		reader = csv.reader(archivoParaLeer)
	
		for item in reader:
			if item[0] == str(id):
				return item
			
#Modificar Producto
def modificarProducto(id, nombre, categoria, precio, stock):
	
	arregloVacio = [ ]
	
	with open(ARCHIVO, "r", newline="", encoding="utf-8") as archivoParaLeer:
		reader = csv.reader(archivoParaLeer)
		for item in reader:
			if item[0] == str(id):
				item[1] = nombre
				item[2] = categoria
				item[3] = precio
				item[4] = stock
			
		arrregloVacio.append(item)
		
		with open(ARCHIVO, "w", nenewline="", encoding= "utf-8") as archivoParaEscribir:
			writer = writer.writerrow(arregloVacio)				


#Eliminar producto
def eliminarProducto(id):
	arregloVacio = [ ]
    
	with open(ARCHIVO, "r", encoding="utf-8") as archivoParaLeer:
		reader = csv.reader(archivoParaLeer)
	
		for item in reader:
			if item[0] != str(id):
				arregloVacio.append(item)
				
	with open(ARCHIVO, "w", newline="", encoding="utf-8") as archivo:
			csv.writer(archivo).writerows(productos)





















