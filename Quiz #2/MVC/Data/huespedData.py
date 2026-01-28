import os
import sys
import csv

from Model.huespedModel import HuespedModel

sys.stdout.reconfigure(encoding = "utf-8")

dir_name = os.path.dirname(os.path.abspath((__file__)))
ARCHIVO = os.path.join(dir_name,'csv','huespedData.csv')

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

def agregarListado(HuespedModel):
	id_quemado = verificarUltimoId()
	ultimoId = id_quemado + 1
	
	HuespedModel.setId(ultimoId)
	
	with open(ARCHIVO, 'a', newline='',encoding='utf-8') as archivo_para_agregar:
		writer = csv.writer(archivo_para_agregar)
		writer.writerow(HuespedModel.importarToCsv())

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
				nombre_en_csv = lista[1].strip().lower()
				nombre_a_buscar = nombre.strip().lower()
				
				if nombre_en_csv == nombre_a_buscar:
					nombreEncontrado.append(lista)
					
	return nombreEncontrado
		
#--------------------------------------------------------------------------------------------------#

def searchId(id):
	if not os.path.exists(ARCHIVO):
		return []
	
	listaVacia = []
	
	with open(ARCHIVO, 'r', newline='',encoding='utf-8') as archivo_para_leer:
		reader = csv.reader(archivo_para_leer)

		for lista in reader:
			if lista:
				if int(lista[0]) == int(lista):
					listaVacia.append(lista)

	return listaVacia
#--------------------------------------------------------------------------------------------------#
#modifica id,nombre,telefono(no lo pide el quiz lo hago para practicar)
def modificarLista(id, HuespedModel): 
	if not os.path.exists(ARCHIVO):
		return []
	
	encontrado = False
	arregloVacio = []
	
	with open(ARCHIVO,'r',newline='',encoding='utf-8') as archivo_para_copiar:
		reader = csv.reader(archivo_para_copiar)
		
		for lista in reader:
			if lista:
				
					if int(lista[0]) == int(id):
						HuespedModel.setId(id)
						nuevo_dato = HuespedModel.importarToCsv()
						arregloVacio.append(nuevo_dato)
						encontrado = True
					else:
						arregloVacio.append(lista)
													
	if encontrado == True:		
		with open(ARCHIVO,'w',newline='',encoding='utf-8') as archivo_para_modificiar:
			writer = csv.writer(archivo_para_modificiar)
			writer.writerows(arregloVacio)
		return encontrado
	else:
		return encontrado
	
#--------------------------------------------------------------------------------------------------#

def eliminarLista(id):
	if not os.path.exists(ARCHIVO):
		return []
	
	encontrado = True
	arregloLista = []

	with open(ARCHIVO,'r',newline='',encoding='utf-8') as archivo_para_leer:
		reader = csv.reader(archivo_para_leer)
		
		for lista in reader:
			if lista:
				try:
					if int(lista[0]) != int(id):
						arregloLista.append(lista)
						encontrado = True
				except ValueError:
					return None
	
	if encontrado == True:
		with open(ARCHIVO,'w',newline='',encoding='utf-8') as archivo_para_sobreEscribir:
			writer = csv.writer(archivo_para_sobreEscribir)
			writer.writerows(arregloLista)
		return encontrado
	else:
		return encontrado


		

	
	
				
	

				