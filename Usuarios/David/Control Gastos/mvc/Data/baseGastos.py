import os
import sys
import csv

sys.stdout.reconfigure(encoding = "utf-8")

BASE_DIR = os.path.dirname(__file__)
ARCHIVO = os.path.join(BASE_DIR, "csv" , "gastos.csv")

#Validar el ultimo ID
def validarUltimoId():
	if not os.path.exists(ARCHIVO):
		return 0
	ultimoId = 0
	
	with open(ARCHIVO, "r" , newline= "", encoding = "utf-8") as archivoParaLeer:
		reader = csv.reader(archivoParaLeer)
		
		for item in reader:
			if item:
				if int(item[0]) > ultimoId:
					ultimoId = int(item[0])
	return ultimoId
#---------------------------------------------------------------------------------------------------------					
#Guardar gastos
def guardarGastos(Gastos):
	ultimoId = validarUltimoId()
	nuevoId = ultimoId  +1
	
	Gastos.setId(nuevoId)
	
	with open(ARCHIVO, "a", newline= "", encoding = "utf-8") as archivoParaLeer:
		writer = csv.writer(archivoParaLeer)
		writer.writerow(Gastos.importToCsv())
#---------------------------------------------------------------------------------------------------------
#Listar gastos
def listarObjeto():
	if not os.path.exists(ARCHIVO):
		return [ ]
	arregloVacio = [ ]
	with open(ARCHIVO, "r", newline= "", encoding= "utf-8") as archivoParaLeer:
		reader = csv.reader(archivoParaLeer)
		
		for item in reader:
			if item:
				arregloVacio.append(item)
				
	return arregloVacio
#---------------------------------------------------------------------------------------------------------				
#Eliminar gastos
def eliminarGastos(id):
	if not os.path.exists(ARCHIVO):
		return [ ]
	arregloVacio = [ ]
	encontrado = False 
	with open(ARCHIVO, "r", newline="", encoding= "utf-8") as archivoParaLeer:
		reader = csv.reader(archivoParaLeer)
		
		for item in reader:
			if int(item[0]) != int(id):
				arregloVacio.append(item)
			else:
				encontrado = True

	if encontrado == True:
		with open(ARCHIVO, "w", newline="", encoding = "utf-8") as archivoParaEscribir:
			writer = csv.writer(archivoParaEscribir)
			writer.writerows(arregloVacio)
			return True
	else:
		return False
#---------------------------------------------------------------------------------------------------------					
					
		
					
					

	