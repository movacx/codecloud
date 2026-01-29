import sys
import os
import csv
from Model.reservaModel import Reserva
sys.stdout.reconfigure(encoding = "utf-8")

BASE_DIR = os.path.dirname(__file__)
ARCHIVO = os.path.join(BASE_DIR, "csv", "reserva.csv")

#Validar ultimoId
def validarUltimoId():
	if not os.path.exists(ARCHIVO):
		return 0 
	ultimoId = 0
	with open(ARCHIVO, "r", nenewline= "", encoding= "utf-8") as archivoParaLeer:
		reader = csv.reader(archivoParaLeer)
		
		for item in reader:
			if int(item[0]) > ultimoId:
				ultimoId = int(item[0])
				
	return ultimoId

#---------------------------------------------------------------------------------------------#
#Registrar reserva
def registrarReserva(Reserva):
	idQuemado = validarUltimoId()
	ultimoId = idQuemado +1 
	
	Reserva.setId(ultimoId)
	
	with open(ARCHIVO, "a" , newline="", enconding = "utf-8") as archivoParaGuardar
	writer = csv.writer(archivoParaGuardar)
	writer.writerow(archivoParaGuardar)
#---------------------------------------------------------------------------------------------#
	
	
	
				
	
