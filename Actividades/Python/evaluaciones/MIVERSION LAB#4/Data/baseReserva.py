import os
import sys
import csv
from datetime import datetime
from Model.reservaModel import Reserva

sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVO = os.path.join(BASE_DIR, "csv", "reservaData.csv")
logFile = os.path.join(BASE_DIR, "log", "logfile.txt")

def guardarError(errorTexto):
    try:
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        mensaje = f'{fecha} ===> {errorTexto}\n'
        
        with open(logFile, 'a', encoding='utf-8') as file:
            file.write(mensaje) 

    except Exception as nombreError:
        print(f'Error critico en log: {nombreError}')

def validarUltimoId():
    if not os.path.exists(ARCHIVO):
        return 0
    
    ultimoId = 0
    
    with open(ARCHIVO, "r", newline="", encoding="utf-8") as archivoParaLeer:
        reader = csv.reader(archivoParaLeer)
        
        for item in reader:
            if item:
                try:
                    id_actual = int(item[0])
                    if id_actual > ultimoId:
                        ultimoId = id_actual
                except ValueError:
                    continue
                    
    return ultimoId

def registrarReserva(reservaObjeto):
    try:
        idQuemado = validarUltimoId()
        ultimoId = idQuemado + 1
        
        reservaObjeto.id = ultimoId
        
        with open(ARCHIVO, "a", newline="", encoding="utf-8") as archivoParaGuardar:
            writer = csv.writer(archivoParaGuardar)
            writer.writerow(reservaObjeto.importarToCsv())
            return True

    except Exception as nombreError:
        guardarError(f'Error al registrar reserva: {nombreError}')
        return False

def listarReservas():
    try:
        if not os.path.exists(ARCHIVO):
            return []
        
        listaReservas = []
        with open(ARCHIVO, "r", newline="", encoding="utf-8") as archivoParaLeer:
            reader = csv.reader(archivoParaLeer)
            for item in reader:
                if item:
                    listaReservas.append(item)
                    
        return listaReservas

    except Exception as nombreError:
        guardarError(f'Error al listar reservas: {nombreError}')
        return []

def buscarReservaPorId(idReserva):
    try:
        if not os.path.exists(ARCHIVO):
            return []
        
        listaEncontrada = []
        
        with open(ARCHIVO, "r", newline="", encoding="utf-8") as archivoParaLeer:
            reader = csv.reader(archivoParaLeer)
            for item in reader:
                if item:
                    try:
                        if int(item[0]) == int(idReserva):
                            listaEncontrada.append(item)
                    except ValueError:
                        continue
                        
        return listaEncontrada

    except Exception as nombreError:
        guardarError(f'Error al buscar reserva por ID: {nombreError}')
        return []

def eliminarReserva(idReserva):
    try:
        if not os.path.exists(ARCHIVO):
            return False
        
        arregloVacio = []
        encontrado = False
        
        with open(ARCHIVO, "r", newline="", encoding="utf-8") as archivoParaLeer:
            reader = csv.reader(archivoParaLeer)
            for item in reader:
                if item:
                    try:
                        if int(item[1]) == int(idReserva):
                            encontrado = True
                        else:
                            arregloVacio.append(item)
                    except ValueError:
                        arregloVacio.append(item)
                    
        if encontrado:
            with open(ARCHIVO, "w", newline="", encoding="utf-8") as archivoParaEscribir:
                writer = csv.writer(archivoParaEscribir)
                writer.writerows(arregloVacio)
            return True
        else:
            return False

    except Exception as nombreError:
        guardarError(f'Error al eliminar reserva: {nombreError}')
        return False

def modificarReserva(idReserva, nuevaHab, nuevoHuesped, nuevaEntrada, nuevaSalida):
    try:
        if not os.path.exists(ARCHIVO):
            return False
        
        arregloVacio = []
        encontrado = False
        
        with open(ARCHIVO, "r", newline="", encoding="utf-8") as archivoParaLeer:
            reader = csv.reader(archivoParaLeer)
            for item in reader:
                if item:
                    try:
                        if int(item[0]) == int(idReserva):
                            item[1] = nuevaHab
                            item[2] = nuevoHuesped
                            item[3] = nuevaEntrada
                            item[4] = nuevaSalida
                            encontrado = True
                        arregloVacio.append(item)
                    except ValueError:
                        arregloVacio.append(item)

        if encontrado:
            with open(ARCHIVO, "w", newline="", encoding="utf-8") as archivoParaEscribir:
                writer = csv.writer(archivoParaEscribir)
                writer.writerows(arregloVacio)
            return True
        else:
            return False

    except Exception as nombreError:
        guardarError(f'Error al modificar reserva: {nombreError}')
        return False