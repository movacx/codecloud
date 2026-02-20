import os
import csv
from datetime import datetime

BASE_DIR = os.path.dirname(__file__)
ARCHIVO = os.path.join(BASE_DIR, "csv", "baseCredito.csv")
logfile = os.path.join(BASE_DIR, "data", "logfile.txt")

#Guardar Error 
def guardarError(errorTexto):
	try:
		fecha = datetime.now().strftime("%Y-%m-%d %H %M %S")
		mensaje = f"{fecha} ===> {errorTexto}\n"
		
		
		with open(ARCHIVO, "a", newline="", encoding="utf-8") as file:
			file.write(mensaje)
			
	except Exception as error:
		print("Error critico en log:", error)
		
#Validar el ultimo ID		
def validarUltimoId():
	try:
		if not os.path.exist(ARCHIVO):
			return 0
		
		ultimoId =0
		
		
		with open(ARCHIVO, "r", newline="", encoding="utf-8") as archivoParaLeer:
			reader = csv.reader(archivoParaLeer)
			
			for item in reader:
				if item:
					idActual = int(item[0])
					if idActual > ultimoId:
						ultimoId = idActual
						
	except Exception as error:
		guardarError(f"Error al validar ultimo id credito: {error}")
		return 0
	
#Registrar Creditos 	
def registrarCredito(credito):
	try:
		idQuemado = validarUltimoId()
		nuevoId = idQuemado +1
		
		credito.setIdCredito(nuevoId)
		
		with open(ARCHIVO, "a", newline="", encoding="utf-8") as archivoParaGuardar:
			writer = csv.writer(archivoParaGuardar)
			writer.writerow(credito.importToCsv)
			return True
		
	except Exception as error:
		guardarError(f"Error critico en registrar credito: {error}")
		return False
	
#Listar Creditos
def listarCreditos():
	try:
		if not os.path.exists(ARCHIVO):
			return [ ]
		
		arregloVacio = [ ]
		with open(ARARCHIVO, "r", newline="", encoding="utf-8") as archivoParaLeer:
			reader = csv.reader(archivoParaLeer)
			
			for item in reader:
				if item:
					arregloVacio.append(item)
		return arregloVacio
		
		
	except Exception as error:
		guardarError(f"Error critico al listar creditos: {error}")
		return [ ]
	
#BuscarCredito	
def buscarCreditoId(idCredito):
	try:
		if not os.path.exists(ARCHIVO):
			return [ ]
		
		
		arregloVacio = [ ]
		
		
		with open(ARCHIVO, "r", newline= "", encoding="utf-8") as archivoParaLeer:
			reader = csv.reader(archivoParaLeer)
			
			for item in reader:
				if int(item[0]) == int(idCredito):
					arregloVacio.append(item)
					
		return arregloVacio
		
	except Exception as error:
		guardarError(f"Error critico al buscar creditos: {error}")
		return [ ]
	
	
#Listar Creditos
def listarCreditosActivos(dniCliente):
	
	try:
		if not os.path.exists(ARCHIVO):
			return [ ]
		
		arregloVacio = [ ]
		
		with open(ARCHIVO, "r", newline="", encoding="utf-8") as archivoParaLeer:
			reader = csv.reader(archivoParaLeer)
			
			for item in reader:
				if item[1] == str(dniCliente) and item[5] == "Activo":
					arregloVacio.append(item)
					
		return arregloVacio
	
	
	except Exception as error:
		guardarError(f"Error critico al listar creditos activos:{error}")
		return [ ]
	
		
#Actualizar credito
def actualizarCredito(idCredito, cuotasPagadas, estado):
	try:
		if not os.path.exists(ARCHIVO):
			return  [ ]
		
		arregloVacio = [ ]
		encontrado = False
		
		with open(ARCHIVO, "r", newline="", encoding = "utf-8") as archivoParaLeer:
			reader = csv.reader(archarchivoParaLeer)
			
			for item in reader:
				if int(item[0]) == int(idCredito):
					item[4] = str(cuotasPagadas)
					item [5] = str(estado)
					arregloVacio.append(item)
					encontrado = True
					
				else:
					arregloVacio.append(item)
					
		if encontrado:
			with open(ARCHIVO, "w", newline="", encoding= "utf-8") as archivoParaGuardar:
				writer = csv.writer(archivoParaGuardar)
				writer.writerows(arregloVacio)
				return True
			
		return False
	
	except Exception as error:
		guardarError(f"Error critico en actualizar credito: {error}")
		return False 
					
#Eliminar credito
def eliminarCredito(idCredito):
	try:
		if not os.path.exists(ARCHIVO):
			return [ ]
		
		encontrado = False
		arregloVacio = [ ]
		
		with open(ARCHIVO, "r", newline="", encoding = "utf-8") as archivoParaLeer:
			reader = csv.reader(archivoParaLeer)
			
			for item in reader:
				if int(item[0]) == int(idCredito):
					encontrado =  True
					
				else:
					arregloVacio.append(item)
					
		if encontrado:
			with open(ARCHIVO, "w", newline="", encoding="utf-8") as archivoParaGuardar:
				writer = csv.writer(archivoParaGuardar)
				writer.writerows(arregloVacio)
				return True
			
			
		return False
	
	except Exception as error:
		guardarError(f"Error critico en eliminar credito: {error}")
		return [ ]
		
					
		
		
		
		
	
	

			
		


