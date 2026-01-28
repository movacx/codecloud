import os
import sys
import csv

from Model.reservaModel import Reserva

sys.stdout.reconfigure(encoding = "utf-8")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVO = os.path.join(BASE_DIR, "csv", "reservas.csv")

#ValidarUltimoID
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
#Registrar reservaciones
def registrarReservacion(Reserva):
	idQuemado = validarUltimoId()
	ultimoId = idQuemado + 1
	
	Reserva.setIde(ultimoId)
	
	with open(ARCHIVO, "a", newline="", encoding = "utf-8") as archivoParaGuardar:
		writer = csv.writer(archivoParaGuardar)
		writer.writerow(Reserva.importarToCsv())
		

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
				encontrado = False
			else:
				encontrado = True
	if encontrado == True:
		with open(ARCHIVO,"w", newline="", encoding = "utf-8") as archivoParaEscribir:
			writer = csv.writer(archivoParaEscribir)
			writer.writerows(arregloVacio)
			return encontrado
	else:
		return encontrado
					



	
	
	