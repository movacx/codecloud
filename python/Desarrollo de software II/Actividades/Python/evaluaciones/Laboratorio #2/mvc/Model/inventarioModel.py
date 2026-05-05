import sys
import os
import csv 

sys.stdout.reconfigure(encoding = "utf-8")

BASE_DIR = os.path.dirname(__file__)
ARCHIVO = os.path.join(BASE_DIR,"CSV", "movimientos.csv")

def guardarMovimiento(id, tipo, cantidad, fecha):
    os.makedirs(os.path.dirname(ARCHIVO), exist_ok=True)
    with open(ARCHIVO, "a", newline= "", encoding = "utf-8") as archivoParaGuardar:
        writer = csv.writer(archivoParaGuardar)
        writer.writerow([id, tipo, cantidad, fecha]) 
        
    print("Datos guardados correctamente en historial ")
        
def listarMovimientos():
    lista = []
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding= "utf-8") as archivoparaleer:
            reader = csv.reader(archivoparaleer)
            for item in reader:
                lista.append(item)
    return lista