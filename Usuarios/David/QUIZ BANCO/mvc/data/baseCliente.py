import os
import csv
from datetime import datetime
#from Model.clienteModel import ClienteModel

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVO = os.path.join(BASE_DIR, "csv", "clientes.csv")
logFile = os.path.join(BASE_DIR, "csv", "logfile.txt")
			
def guardarError(errorTexto):
	try:
		fecha = datatime.now().strftime("%Y-m%-%d %H: %M: %S")
		mensaje = f"{fecha} ===> {errorTexto}\n"
		
		with open(logFile, "a", newline="", encoding = "utf-8") as file:
			file.write(mensaje)
			
	except Exception as error:
		print("Error Critico en el log: ", error)
		
def guardarCliente():
	try:
		if not os.path.exists(ARCHIVO):
			return False
		
		if buscarCliente(cliente.dni):
			return False
		
		with open(ARCHIVO, "a", newline="", encoding="utf-8") as archivoParaGuardar:
			writer = csv.writer(archivoParaGuardar)
			writer.writerow(cliente.importarToCsv())
			return True
	
	except Exception as error:
		guardarError(f"Error al registrar cliente: {error}")
		return False
	
	
def listarClientes():
	try:
		if not os.path.exists(ARCHIVO):
			return [ ]
		lista = [ ]
		
		with open(ARCHIVO, "r", newline="", encoding="utf-8") as archivoParaLeer:
			reader = csv.reader(archivoParaLeer)
			
			for item in reader:
				if item:
					lista.append(item)
		return lista
	
	except Exception as error:
		guardarError(f"Error al listar clientes: {error}")
		return [ ]

def buscarCliente(dniCliente):
	try:
		if not os.path.exists(ARCHIVO):
			return [ ]
		
		encontrado = [ ]
		
		with open(ARCHIVO, "r", newline="", encoding="utf-8") as archivoParaLeer:
			reader = csv.reader(aarchivoParaLeer)
			
			for item in reader:
				if int(item[0]) == dniCliente:
					encontrado.append(item)
					
			return encontrado
		
	except Exception as error:
		guardarError(f"Error al buscar cliente: {error}")
		return [ ]
	

def eliminarCliente(dniCliente):
	try:
		if not os.path.exists(ARCHIVO):
			return [ ]
		
		arregloVacio = [ ]
		encontrado = False
		
		with open(ARCHIVO, "r", newline="", enconding= "utf-8") as archivoParaLeer:
			reader = csv.reader(archivoParaLeer)
			
			for item in reader:
				if int(item[0]) == dniCliente:
					encontrado = True
				else:
					arregloVacio.append(item)
					
		if encontrado:
			with open(ARCHIVO, "w", newline="", encoding= "utf-8") as archivoParaEscribir:
				writer = csv.writer(archivoParaEscribir)
				writer.writerows(arregloVacio)
				
			return True
		
		return False
	
	except Exception as error:
		guardarError(f"Error al eliminar cliente: {error}")
		return False 
					
					
		
					
		
	
	
	
						   