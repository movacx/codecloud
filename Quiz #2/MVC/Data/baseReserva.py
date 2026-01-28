import os
import sys
import csv
from Model.reservaModel import Reserva

sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVO = os.path.join(BASE_DIR, "csv", "reservaData.csv")

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

def registrarReserva(reservaObjeto):
    idQuemado = validarUltimoId()
    ultimoId = idQuemado + 1
    

    reservaObjeto.id = ultimoId
    

    with open(ARCHIVO, "a", newline="", encoding="utf-8") as archivoParaGuardar:
        writer = csv.writer(archivoParaGuardar)
        writer.writerow(reservaObjeto.importarToCsv())

def listarReservas():
    if not os.path.exists(ARCHIVO):
        return []
    
    listaReservas = []
    with open(ARCHIVO, "r", newline="", encoding="utf-8") as archivoParaLeer:
        reader = csv.reader(archivoParaLeer)
        for item in reader:
            listaReservas.append(item)
    return listaReservas

def buscarReservaPorId(idReserva):
    if not os.path.exists(ARCHIVO):
        return None
    
    with open(ARCHIVO, "r", newline="", encoding="utf-8") as archivoParaLeer:
        reader = csv.reader(archivoParaLeer)
        for item in reader:
            if item and int(item[0]) == int(idReserva):
                return item
    return None

def eliminarReserva(idReserva):
    if not os.path.exists(ARCHIVO):
        return False
    
    arregloVacio = []
    encontrado = False
    
    with open(ARCHIVO, "r", newline="", encoding="utf-8") as archivoParaLeer:
        reader = csv.reader(archivoParaLeer)
        for item in reader:
            if item:
                if int(item[0]) != int(idReserva):
                    arregloVacio.append(item)
                else:
                    encontrado = True
                
    if encontrado:
        with open(ARCHIVO, "w", newline="", encoding="utf-8") as archivoParaEscribir:
            writer = csv.writer(archivoParaEscribir)
            writer.writerows(arregloVacio)
            
    return encontrado

