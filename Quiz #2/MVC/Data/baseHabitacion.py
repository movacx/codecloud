import os
import sys
import csv

from Model.habitacionModel import Habitacion

sys.stdout.reconfigure(encoding = "utf-8")

BASE_DIR = os.path.dirname(__file__)
ARCHIVO = os.path.join(BASE_DIR, "csv", "habitacion.csv")

#ValidarUltimoID
def validarUltimoId():
	if not os.path.exists(ARCHIVO):
		return 0
	
	ultimoId = 0
	
	with open(ARCHIVO, "r", newline="", encoding="utf-8") as archivoParaLeer:
		reader = csv.reader(archivoParaLeer)

		for item in reader:
			if item:
				if int(item[0]) > int(id):
					ultimoId = int(item[0])
			
	return ultimoId	
#Registrar habitaciones
def registrarHabitacion(Habitacion):
	if not os.path.exists(ARCHIVO):
		return 0
	idQuemado = verificarUltimoId()
	ultimoId = idQuemado + 1
	
	Habitacion.setId(ultimoId)
	
	with open(ARCHIVO, "a", newline="", encoding = "utf-8") as archivoParaGuardar:
		writer = csv.writer(archivoParaGuardar)
		writer.writerow(Habitacion.importarToCsv())
		

#Listar habitaciones
def listarHabitaciones():
	if not os.path.exists(ARCHIVO):
		return 0 
	listaVacia = [ ]
	
	with open(ARCHIVO, "r", newline= "", encoding= "utf-8") as archivoParaLeer:
		reader = csv.reader(archivoParaLeer)
		
		for item in reader:
			listaVacia.append(item)
			
	return listaVacia

#Buscar por número
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

#Cambiar estado “Disponible/Ocupada”
def modificarEstado(id, estado):
	if not os.path.exists(ARCHIVO):
		return 0
	
	encontrado = False 
	arregloVacio = [ ] 
	with open(ARCHIVO, "r", newline= "", encoding= "utf-8") as archivoParaLeer:
		reader = csv.reader(archivoParaLeer)
		
		for item in reader:
			if item:
				try:
					if int(item[0]) != int(id):
						item[4] = estado
						arregloVacio.append(item)
					else:
						arregloVacio.append(item)
				except ValueError:
					arregloVacio.append(item)
		return "No hay ninguna habitacion agregada"
	
	with open(ARCHIVO, "w", newline= "", encoding= "utf-8") as archivoParaEscribir:
		writer = csv.writer(archivoParaEscribir)
		writer.writerows(arregloVacio)
		return "Estado modificado"
	
	
#Ordenar por precio (usar Bubble Sort o sort())
def ordenarPrecio():
    listaHabitaciones = listarHabitaciones()
    listaTemporalOrden = []

    for item in listaHabitaciones:
        listaTemporalOrden.append([
            float(item[3]),  # precio primero
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



	
	
	