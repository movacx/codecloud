import os
import sys
import csv
from Model.reservaModel import Reserva

sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Asegurate de crear la carpeta csv si no existe
ARCHIVO = os.path.join(BASE_DIR, "csv", "reservaData.csv")

# --- Validar Ultimo ID ---
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

# --- Registrar Reserva ---
def registrarReserva(reservaObjeto):
    # Generamos ID automatico
    idQuemado = validarUltimoId()
    ultimoId = idQuemado + 1
    
    # Asignamos el ID al objeto (tu modelo tiene self.id)
    reservaObjeto.id = ultimoId
    
    # Guardamos
    with open(ARCHIVO, "a", newline="", encoding="utf-8") as archivoParaGuardar:
        writer = csv.writer(archivoParaGuardar)
        writer.writerow(reservaObjeto.importarToCsv())

# --- Listar Reservas ---
def listarReservas():
    if not os.path.exists(ARCHIVO):
        return []
    
    listaReservas = []
    with open(ARCHIVO, "r", newline="", encoding="utf-8") as archivoParaLeer:
        reader = csv.reader(archivoParaLeer)
        for item in reader:
            listaReservas.append(item)
    return listaReservas

# --- Buscar Reserva por ID (IMPORTANTE PARA ELIMINAR Y LIBERAR) ---
def buscarReservaPorId(idReserva):
    if not os.path.exists(ARCHIVO):
        return None
    
    with open(ARCHIVO, "r", newline="", encoding="utf-8") as archivoParaLeer:
        reader = csv.reader(archivoParaLeer)
        for item in reader:
            if item and int(item[0]) == int(idReserva):
                return item # Retorna la lista con los datos
    return None

# --- Eliminar Reserva ---
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

