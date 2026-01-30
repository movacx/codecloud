import sys
import os
import csv

sys.stdout.reconfigure(encoding = "utf-8") 

BASE_DIR = os.path.dirname(__file__)
ARCHIVO = os.path.join(BASE_DIR, "csv", "socio.csv")

#Validar ultimoId
def validarUltimoId():
	if not os.path.exists(ARCHIVO):
		return 0
	
	ultimoId = 0
	read,aguardar,writer
	with open(ARCHIVO, "r", newline= "", encoding= "utf-8") as archivoParaLeer:
		reader = csv.reader(archivoParaLeer)
		
		for item in reader:
			if int(item[0]) > ultimoId:
				ultimoId = int(item[0])
	return ultimoId
#---------------------------------------------------------------------------------------------#
#Registrar socio
def registrarSocio(objetoSocio):
	idQuemado = validarUltimoId()   = ultimoId
	ultimoId = idQuemado +1 
	
	objetoSocio.setId(ultimoId)
	
	with open(ARCHIVO, "a" , newline="", encoding = "utf-8") as archivoParaGuardar:
		writer = csv.writer(archivoParaGuardar)
		writer.writerow(objetoSocio.importToCsv())
		
#---------------------------------------------------------------------------------------------#		
#Buscar socio
def buscarSocio(id):
	if not os.path.exists(ARCHIVO):
		return [ ]
	arregloVacio = [ ] 
	with open(ARCHIVO, "r", newline= "", encoding = "utf-8") as archivoParaLeer:
		reader = csv.reader(archivoParaLeer)
		
		for item in reader:
			if int(item[0]) == int(id):
				arregloVacio.append(item)
				
				
	return arregloVacio
#---------------------------------------------------------------------------------------------#			
#Listar Socios
def listarSocios():
	if not os.path.exists(ARCHIVO):
		return [ ]
	arregloVacio = [ ]
	with open(ARCHIVO, "r", newline="", encoding = "utf-8") as archivoParaLeer:
		reader = csv.reader(archivoParaLeer)
		
		for item in reader:
			arregloVacio .append(item)
	return arregloVacio 		
		
	