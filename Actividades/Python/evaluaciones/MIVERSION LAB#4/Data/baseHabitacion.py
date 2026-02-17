import os
import sys
import csv
from datetime import datetime
from Model.habitacionModel import HabitacionModel

sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVO = os.path.join(BASE_DIR, "csv", "habitacionData.csv")
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

def registrarHabitacion(Habitacion):
    try:
        idQuemado = validarUltimoId()
        ultimoId = idQuemado + 1
        
        Habitacion.setIde(ultimoId)
        
        with open(ARCHIVO, "a", newline="", encoding = "utf-8") as archivoParaGuardar:
            writer = csv.writer(archivoParaGuardar)
            writer.writerow(Habitacion.importarToCsv())
            return True

    except Exception as nombreError:
        guardarError(f'Error al registrar habitacion: {nombreError}')
        return False
        
def listarHabitaciones():
    try:
        if not os.path.exists(ARCHIVO):
            return []
        
        listaVacia = []
        
        with open(ARCHIVO, "r", newline= "", encoding= "utf-8") as archivoParaLeer:
            reader = csv.reader(archivoParaLeer)
            
            for item in reader:
                if item:
                    listaVacia.append(item)
                
        return listaVacia

    except Exception as nombreError:
        guardarError(f'Error al listar habitaciones: {nombreError}')
        return []

def buscarHabitacionId(id):
    try:
        if not os.path.exists(ARCHIVO):
            return []
        
        habitacionEncontrada = []
        with open(ARCHIVO, "r", newline="", encoding= "utf-8") as archivoParaLeer:
            reader = csv.reader(archivoParaLeer)
            
            for item in reader:
                if item:
                    try:
                        if int(item[1]) == int(id):
                            habitacionEncontrada.append(item)
                    except ValueError:
                        continue
        return habitacionEncontrada

    except Exception as nombreError:
        guardarError(f'Error al buscar habitacion por ID: {nombreError}')
        return []

def modificar(id, estado): 
    try:
        if not os.path.exists(ARCHIVO):
            return False
        
        encontrado = False
        arregloVacio = []
        
        with open(ARCHIVO,'r',newline='',encoding='utf-8') as archivoParaLeer:
            reader = csv.reader(archivoParaLeer)
            
            for item in reader:
                if item:
                    try:
                        if int(item[1]) == int(id):
                            item[4] = estado
                            arregloVacio.append(item)
                            encontrado = True
                        else:
                            arregloVacio.append(item)
                    except ValueError:
                        arregloVacio.append(item)
                                                        
        if encontrado:      
            with open(ARCHIVO,'w',newline='',encoding='utf-8') as archivoParaEscribir:
                writer = csv.writer(archivoParaEscribir)
                writer.writerows(arregloVacio)
            return True
        else:
            return False

    except Exception as nombreError:
        guardarError(f'Error al modificar estado habitacion: {nombreError}')
        return False

def eliminarHabitacion(idHabitacion):
    try:
        if not os.path.exists(ARCHIVO):
            return False
        
        arregloVacio = []
        encontrado = False

        with open(ARCHIVO, "r", newline= "", encoding = "utf-8") as archivoParaLeer:
            reader = csv.reader(archivoParaLeer)
            
            for item in reader:
                if item:
                    try:
                        if int(item[1]) == int(idHabitacion):
                            encontrado = True
                        else:
                            arregloVacio.append(item)
                    except ValueError:
                        arregloVacio.append(item)

        if encontrado:
            with open(ARCHIVO,"w", newline="", encoding = "utf-8") as archivoParaEscribir:
                writer = csv.writer(archivoParaEscribir)
                writer.writerows(arregloVacio)
            return True
        else:
            return False

    except Exception as nombreError:
        guardarError(f'Error al eliminar habitacion: {nombreError}')
        return False

def ordenarPrecio():
    try:
        listaHabitaciones = listarHabitaciones()
        listaTemporalOrden = []

        for item in listaHabitaciones:
            try:
                listaTemporalOrden.append([
                    float(item[3]),
                    item[0],
                    item[1],
                    item[2],
                    item[4]
                ]) 
            except ValueError:
                continue

        listaTemporalOrden.sort()

        listaHabitacionesOrdenadas = []

        for item in listaTemporalOrden:
            listaHabitacionesOrdenadas.append([
                item[1],
                item[2],
                item[3],
                item[0],
                item[4]
            ])

        return listaHabitacionesOrdenadas

    except Exception as nombreError:
        guardarError(f'Error al ordenar habitaciones: {nombreError}')
        return []