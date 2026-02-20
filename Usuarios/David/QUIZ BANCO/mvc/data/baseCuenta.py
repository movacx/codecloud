import os
import csv
from datetime import datetime

BASE_DIR= os.path.dirname(__file__)
ARCHIVO = os.path.join(BASE_DIR, "csv", "baseCuenta.csv")
logFile = os.path.join(BASE_DIR, "csv", "logfile.txt")


def guardarError(errorTexto):
	try:
		fecha = datetime.now().strftime("%Y-%m%-%d %H %M %S")
		mensaje = f"{fecha} ===> {errorTexto}\n"
		
		with open(ARCHIVO, "a", newline="", encoding="utf-8") as file:
			file.write(mensaje)
			
			
	except Exception as error:
		print("Error Critico en log:", error)
		
		
		
def registrarCuenta(cuenta):
	try:
		if buscarCuentaPorNumero(cuenta.numeroCuenta):
			return False
		
		with open(ARCHIVO, "a", newline= "", encoding = "utf-8") as archivoParaGuardar:
			writer = csv.writer(archivoParaGuardar)
			writer.writerow(cuenta.importToCsv())
			return True		
	except  Exception as error:
		guardarError(f"Error al registrar Cuenta: {error}")
		return False
	
	
def listarCuentas():
	try:
		if not os.path.exist(ARCHIVO):
			return [ ]
		
		arregloVacio = [ ]
		
		with open(ARCHIVO, "r", newline="", encoding="utf-8") as archivoParaLeer:
			reader = csv.reader(archivoParaLeer)
			
			for item in reader:
				if item:
					arregloVacio.append(item)
										
		return arregloVacio
										
	except Exception as error:
		guardarError(f"Error al listar cuentas: {error}")
		return []
	

def buscarCuentaPorNumero(numeroCuenta):
	try:
		if not os.path.exist(ARCHIVO):
			return []
		
		arregloVacio = [ ]
		
		with open(ARCHIVO, "r", newline= "", encoding = "utf-8") as archivoParaLeer:
			reader = csv.reader(archivoParaLeer)
			
			for item in reader:
				if int(item[1]) == int(numeroCuenta):
					arregloVacio.append(item)
					
			return arregloVacio
		
	except Exception as error:
		guardarError(f"Error al buscar cuenta: {error}")
		return []
	


def actualizarSaldo(numeroCuenta, nuevoSaldo):
	try:
		if not os.path.exist(ARCHIVO):
			return []
		
		encontrado = False
		arregloVacio = []
		
		with open(ARCHIVO, "r", newline="", encoding="utf-8") as archivoParaLeer:
			reader = csv.reader(archivoParaLeer)
			
			for item in reader:
				if item[1]== numeroCuenta:
					item[3] = str(nuevoSaldo)
					arregloVacio.append(item)
					encontrado = True
					
				else:
					arregloVacio.append(item)
					
		if encontrado:
			with open(ARCHIVO, "w", newline="", encoding="utf-8") as archivoParaGuardar:
				writer = csv.writer(archivoParaGuardar)
				writer.writerows(arregloVacio)
				return True
			
		return False
	except Exception as error:
		guardarError(f"Error al actualizar saldo: {error}")
		return []
	
	
def eliminarCuenta(numeroCuenta):
	try:
		if not os.path.exists(ARCHIVO):
			return [ ]
		
		arregloVacio = [ ]
		encontrado = False
		
		with open(ARCHIVO, "r", newline="", enconding= "utf-8") as archivoParaLeer:
			reader = csv.reader(archivoParaLeer)
			
			for item in reader:
				if item[1] == numeroCuenta:
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
		guardarError(f"Error al eliminar cuenta: {error}")
		return False 
					
			
	
	
		