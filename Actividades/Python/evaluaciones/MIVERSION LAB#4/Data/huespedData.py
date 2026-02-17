import os
import sys
import csv
from datetime import datetime

sys.stdout.reconfigure(encoding="utf-8")

dir_name = os.path.dirname(os.path.abspath(__file__))
ARCHIVO = os.path.join(dir_name, 'csv', 'huespedData.csv')
logFile = os.path.join(dir_name, 'log', 'logfile.txt')

def guardarError(errorTexto):
    try:
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        mensaje = f'{fecha} ===> {errorTexto}\n'
        
        with open(logFile, 'a', encoding='utf-8') as file:
            file.write(mensaje) 

    except Exception as nombreError:
        print(f'Error critico en log: {nombreError}')

def verificarUltimoId():
    if not os.path.exists(ARCHIVO):
        return 0
    
    ultimoId = 0
    
    with open(ARCHIVO, 'r', newline='', encoding='utf-8') as archivo_para_leer:
        reader = csv.reader(archivo_para_leer)
        
        for lista in reader:
            if lista:
                try:
                    id_actual = int(lista[0])
                    if id_actual > ultimoId:
                        ultimoId = id_actual
                except ValueError:
                    continue 
                    
    return ultimoId

def agregarListado(HuespedModel):
    try:
        id_quemado = verificarUltimoId()
        ultimoId = id_quemado + 1
        HuespedModel.setId(ultimoId)
        
        with open(ARCHIVO, 'a', newline='', encoding='utf-8') as archivo_para_agregar:
            writer = csv.writer(archivo_para_agregar)
            writer.writerow(HuespedModel.importarToCsv())
            return True 

    except Exception as nombreError: 
        guardarError(f'Error al cargar los datos: {nombreError}')
        return False

def listarTodos():
    try:
        if not os.path.exists(ARCHIVO):
            return []
        
        copiarLista = []
        with open(ARCHIVO, 'r', newline='', encoding='utf-8') as archivo_para_leer:
            reader = csv.reader(archivo_para_leer)
            for lista in reader:
                if lista:
                    copiarLista.append(lista)
                    
        return copiarLista
    
    except Exception as nombreError:
        guardarError(f'Error al mostrar los datos: {nombreError}')
        return False

def searchName(nombre):
    try:
        if not os.path.exists(ARCHIVO):
            return []
        
        nombreEncontrado = []
        
        with open(ARCHIVO, 'r', newline='', encoding='utf-8') as archivo_para_leer:
            reader = csv.reader(archivo_para_leer)
            
            for lista in reader:
                if lista:
                    nombre_en_csv = lista[1].strip().lower()
                    nombre_a_buscar = nombre.strip().lower()
                    
                    if nombre_en_csv == nombre_a_buscar:
                        nombreEncontrado.append(lista)
                        
        return nombreEncontrado
    
    except Exception as nombreError:
        guardarError(f'Error al buscar el dato: {nombreError}')
        return []

def searchId(id):
    try:
        if not os.path.exists(ARCHIVO):
            return []
        
        listaEncontrada = []
        
        with open(ARCHIVO, 'r', newline='', encoding='utf-8') as archivo_para_leer:
            reader = csv.reader(archivo_para_leer)

            for lista in reader:
                if lista:
                    try:
                        if int(lista[0]) == int(id):
                            listaEncontrada.append(lista)
                    except ValueError:
                        continue 

        return listaEncontrada

    except Exception as nombreError:
        guardarError(f'Error al buscar por ID: {nombreError}')
        return []

def modificarLista(id, HuespedModel): 
    try:
        if not os.path.exists(ARCHIVO):
            return False 
        
        encontrado = False
        arregloVacio = []
        
        with open(ARCHIVO, 'r', newline='', encoding='utf-8') as archivo_para_copiar:
            reader = csv.reader(archivo_para_copiar)
            
            for lista in reader:
                if lista:
                    try:
                        if int(lista[0]) == int(id):
                            HuespedModel.setId(id) 
                            nuevo_dato = HuespedModel.importarToCsv()
                            arregloVacio.append(nuevo_dato)
                            encontrado = True
                        else:
                            arregloVacio.append(lista)
                    except ValueError:
                        arregloVacio.append(lista) 
                                                        
        if encontrado:      
            with open(ARCHIVO, 'w', newline='', encoding='utf-8') as archivo_para_modificiar:
                writer = csv.writer(archivo_para_modificiar)
                writer.writerows(arregloVacio)
            return True
        else:
            return False

    except Exception as nombreError:
        guardarError(f'Error al modificar la lista: {nombreError}')
        return False
    
def eliminarLista(nombre):
    try:
        if not os.path.exists(ARCHIVO):
            return False
        
        encontrado = False 
        arregloLista = []

        with open(ARCHIVO, 'r', newline='', encoding='utf-8') as archivo_para_leer:
            reader = csv.reader(archivo_para_leer)
            
            for lista in reader:
                if lista:
                    try:
                        if str(lista[1]) == str(nombre):
                            encontrado = True 
                        else:
                            arregloLista.append(lista) 
                    except ValueError:
                        arregloLista.append(lista)
        
        if encontrado:
            with open(ARCHIVO, 'w', newline='', encoding='utf-8') as archivo_para_sobreEscribir:
                writer = csv.writer(archivo_para_sobreEscribir)
                writer.writerows(arregloLista)
            return True
        else:
            return False

    except Exception as nombreError:
        guardarError(f'Error al eliminar de la lista: {nombreError}')
        return False