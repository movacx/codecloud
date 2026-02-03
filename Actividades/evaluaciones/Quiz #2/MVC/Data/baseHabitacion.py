import os
import sys
import csv
from datetime import datetime

#from Model.habitacionModel import HabitacionModel

sys.stdout.reconfigure(encoding = "utf-8")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVO = os.path.join(BASE_DIR, "csv", "habitacionData.csv")
LogFile = os.path.join(BASE_DIR, "log", "errores.txt")
#-----------------------------------------------------------------------------------------#
def validarUltimoId():
	if not os.path.exists(ARCHIVO):
		return 0
	
	ultimoId = 0
	
	with open(ARCHIVO, "r", newline="", encoding="utf-8") as archivoParaLeer:
		reader = csv.reader(archivoParaLeer)

		for item in reader:
			if item:
				if int(item[0]) > ultimoId:
					ultimoId = int(item[0])
			
	return ultimoId	
#-----------------------------------------------------------------------------------------#
def guardarError(errorTexto):
	try:
		fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		with open(LogFile, "a", newline= "", encoding= "utf-8") as file:
			file.write("f{fecha} --> {errorTexto}\n")
	except Exception as nombreError:
		guardarError(f"Error fatal al guardar logs {nombreError} ")
        
#-----------------------------------------------------------------------------------------#
def cargar():
	try:
		if not os.path.exists(LogFile):
			return
		with open(ARCHIVO, "r", encoding="utf-8") as file:
			reader = csv.reader(file)
			for numero, tipo, precio, estado in reader:
				self.habitaciones.append(Habitacion(numero, tipo, precio, estado))
           
	except Exception as nombreError:
		guardarError(f"Error fatal al guardar logs {nombreError} ")
#-----------------------------------------------------------------------------------------#           
def registrarHabitacion(Habitacion):
	try:
		idQuemado = validarUltimoId()
		ultimoId = idQuemado + 1
		
		Habitacion.setIde(ultimoId)
		
		with open(ARCHIVO, "a", newline="", encoding = "utf-8") as archivoParaGuardar:
			writer = csv.writer(archivoParaGuardar)
			writer.writerow(Habitacion.importarToCsv())
	except Exception as nombreError:
		guardarError(f"Error fatal al guardar logs {nombreError} ")
#-----------------------------------------------------------------------------------------#
def listarHabitaciones():
	try:
		if not os.path.exists(ARCHIVO):
			return 0 
		listaVacia = [ ]
		
		with open(ARCHIVO, "r", newline= "", encoding= "utf-8") as archivoParaLeer:
			reader = csv.reader(archivoParaLeer)
			
			for item in reader:
				listaVacia.append(item)
				
		return listaVacia
	except Exception as nombreError:
		guardarError("fError fatal al listar habitaciones {nombreError} ")
#-----------------------------------------------------------------------------------------#
def buscarHabitacionId(id):
	try:
		if not os.path.exists(ARCHIVO):
			return 0
		
		encontrado = False 
		habitacionEncontrada = [ ]
		with open(ARCHIVO, "r", newline="", encoding= "utf-8") as archivoParaLeer:
			reader = csv.reader(archivoParaLeer)
			
			for item in reader:
				if item:
					if int(item[0]) == int(id):
						encontrado = True 
						habitacionEncontrada.append(item)
		return habitacionEncontrada
	except Exception as nombreError:
		guardarError("fError fatal al buscar habitaciones {nombreError} ")
#-----------------------------------------------------------------------------------------#
def modificar(id, estado):
	try:
		if not os.path.exists(ARCHIVO):
			return []
		
		encontrado = False
		arregloVacio = []
		
		with open(ARCHIVO,'r',newline='',encoding='utf-8') as archivoParaLeer:
			reader = csv.reader(archivoParaLeer)
			
			for item in reader:
				if item:
					
						if int(item[0]) == int(id):
							item[4] = estado 
							arregloVacio.append(item)
							encontrado = True
						else:
							arregloVacio.append(item)
														
		if encontrado == True:		
			with open(ARCHIVO,'w',newline='',encoding='utf-8') as archivoParaEscribir:
				writer = csv.writer(archivoParaEscribir)
				writer.writerows(arregloVacio)
			return encontrado
		else:
			return encontrado
	except Exception as nombreError:
		guardarError("fError fatal al modificar habitaciones {nombreError} ")

#-----------------------------------------------------------------------------------------#	
def eliminarHabitacion(idHabitacion):
	try:
		if not os.path.exists(ARCHIVO):
			return [ ]
		
		arregloVacio = [ ]
		encontrado = False
		with open(ARCHIVO, "r", newline= "", encoding = "utf-8") as archivoParaLeer:
			reader = csv.reader(archivoParaLeer)
			
			for item in reader:
				if int(item[0]) != int(idHabitacion):
					arregloVacio.append(item)
				else:
					encontrado = True
		if encontrado == True:
			with open(ARCHIVO,"w", newline="", encoding = "utf-8") as archivoParaEscribir:
				writer = csv.writer(archivoParaEscribir)
				writer.writerows(arregloVacio)
				return encontrado
		else:
			return encontrado
	except  Exception as nombreError:
		guardarError("fError fatal al modificar habitaciones {nombreError} ")


#-----------------------------------------------------------------------------------------#	

def ordenarPrecio():
    listaHabitaciones = listarHabitaciones()
    listaTemporalOrden = []

    for item in listaHabitaciones:
        listaTemporalOrden.append([
            float(item[3]), 
            item[0],
            item[1],
            item[2],
            item[4]
        ]) 

    listaTemporalOrden.sort()

    listaHabitacionesOrdenadas = []

    for item in listaTemporalOrden:
        listaHabitacionesOrdenadas.append([
            item[1],
            item[2],
            item[3],
            item[0],
            item[4]
        ])

    return listaHabitacionesOrdenadas

#-----------------------------------------------------------------------------------------#	


					