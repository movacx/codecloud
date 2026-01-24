import sys
import os

sys.stdout.reconfigure(enconding = "utf-8")

import csv 

BASE_DIR = os.path.dirname(__file__)
ARCHIVO = os.path.join(BASE_DIR,"CSV", "movimientos.csv")

#Registrar movimiento
def guaradarMovimiento(id, tipo, cantidad):

    with open(ARCHIVO, "a", newline= "", encoding = "utf-8") as archivoParaGuardar:
        writer = csv.writer(archivoParaGuardar)
        writer.writerow([id, tipo, cantidad]) 
        
        print("Datos guardatos correctamente")
        
#Listar movimiento
def listarMovimiento():
	with open(ARCHIVO, "r", enconding= "utf-8") as archivoparaleer:
		reader = csv.reader(archivoparaleer)
		for item in reader:
			print(item)
