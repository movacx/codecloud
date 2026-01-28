import os
import sys
import csv

from Model.reservaModel import ReservaModel

sys.stdout.reconfigure(encoding = "utf-8")

dir_name = os.path.dirname(os.path.abspath((__file__)))
ARCHIVO = os.path.join(dir_name,'csv','baseReserva.csv')

#--------------------------------------------------------------------------------------------------#

def verificarUltimoId():
	if not os.path.exists(ARCHIVO):
		return 0
	
	ultimoId = 0
	
	with open(ARCHIVO,'r', newline='',encoding='utf-8') as archivo_para_leer:
		reader = csv.reader(archivo_para_leer)
		
		for lista in reader:
			if lista:
				if int(lista[0]) > ultimoId:
					ultimoId = int(lista[0])
	return ultimoId

#--------------------------------------------------------------------------------------------------#

def agregarListado(ReservaModel):
	id_quemado = verificarUltimoId()
	ultimoId = id_quemado + 1
	
	ReservaModel.setId(ultimoId)
	
	with open(ARCHIVO, 'a', newline='',encoding='utf-8') as archivo_para_agregar:
		writer = csv.writer(archivo_para_agregar)
		writer.writerow(ReservaModel.importarToCsv())

#--------------------------------------------------------------------------------------------------#

def listarTodos():
	if not os.path.exists(ARCHIVO):
		return []
	
	copiarLista = []
	with open(ARCHIVO,'r',newline='',encoding='utf-8') as archivo_para_leer:
		reader = csv.reader(archivo_para_leer)
		for lista in reader:
			if lista:
				copiarLista.append(lista)
				
	return copiarLista

#--------------------------------------------------------------------------------------------------#

def searchName(nombre):
	if not os.path.exists(ARCHIVO):
		return []
	
	nombreEncontrado = []
	
	with open(ARCHIVO, 'r', newline='',encoding='utf-8') as archivo_para_leer:
		reader = csv.reader(archivo_para_leer)
		
		for lista in reader:
			if lista:
				nombre_en_csv = lista[2].strip().lower()
				nombre_a_buscar = nombre.strip().lower()
				
				if nombre_en_csv == nombre_a_buscar:
					nombreEncontrado.append(lista)
					
	return nombreEncontrado
		
#--------------------------------------------------------------------------------------------------#


