import os
import sys
import csv

from Model.habitacionModel import HabitacionModel

sys.stdout.reconfigure(encoding = "utf-8")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVO = os.path.join(BASE_DIR, "csv", "habitacionData.csv")

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
def registrarHabitacion(Habitacion):
	idQuemado = validarUltimoId()
	ultimoId = idQuemado + 1
	
	Habitacion.setIde(ultimoId)
	
	with open(ARCHIVO, "a", newline="", encoding = "utf-8") as archivoParaGuardar:
		writer = csv.writer(archivoParaGuardar)
		writer.writerow(Habitacion.importarToCsv())
		
#-----------------------------------------------------------------------------------------#
def listarHabitaciones():
	if not os.path.exists(ARCHIVO):
		return 0 
	listaVacia = [ ]
	
	with open(ARCHIVO, "r", newline= "", encoding= "utf-8") as archivoParaLeer:
		reader = csv.reader(archivoParaLeer)
		
		for item in reader:
			listaVacia.append(item)
			
	return listaVacia
#-----------------------------------------------------------------------------------------#
def buscarHabitacionId(id):
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
#-----------------------------------------------------------------------------------------#
def modificar(id, estado): 
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

#-----------------------------------------------------------------------------------------#	

def eliminarHabitacion(idHabitacion):
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


					