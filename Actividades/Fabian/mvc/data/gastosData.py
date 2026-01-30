    #    Reto 1: Crear la función validarUltimoId (como ya sabes) para que los IDs no se repitan.
    #    Reto 2: Función guardarGasto que reciba el objeto, le asigne ID y escriba una nueva línea.
    #    Reto 3: Función listarGastos que devuelva todas las filas del CSV.
    #    Reto 4: Función eliminarGasto que reescriba el archivo ignorando el ID borrado.

import os
import sys
import csv

base_dir = os.path.dirname(os.path.abspath(__file__))
ARCHIVO = os.path.join(base_dir,'csv','registroGastos.csv')


#‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾#
def validarUltimoId():
    if not os.path.exists(ARCHIVO):
        return 0
    
    ultimoId = 0
    
    with open(ARCHIVO, 'r', newline = '', encoding='utf-8') as archivo_para_copiar:
        reader = csv.reader(archivo_para_copiar)
        for lista in reader:
            if lista:
                if int(lista[0]) > ultimoId:
                    ultimoId = int(lista[0])
                    
    return ultimoId

#‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾#
def addList(objetoModel):
    ultimoId = validarUltimoId()
    nuevoId = ultimoId + 1

    objetoModel.setId(nuevoId)
    
    with open(ARCHIVO, 'a', newline = '', encoding = 'utf-8') as new_file:
        writer = csv.writer(new_file)
        writer.writerow(objetoModel.importTocsv())
        return True

#‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾#
def searhList():
    if not os.path.exists(ARCHIVO):
        return []
    
    copia_csv = []
    
    with open(ARCHIVO, 'r', newline = '', encoding = 'utf-8') as archivo_para_leer:
        reader = csv.reader(archivo_para_leer)
        
        for lista in reader:
            if lista:
                copia_csv.append(lista)
    
    return copia_csv

#‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾#
def deleteList(id):
    
    arregloVacio = []
    encontrado = False
    
    with open(ARCHIVO, 'r', newline = '', encoding = 'utf-8') as archivo_para_copiar:
        reader = csv.reader(archivo_para_copiar)
        
        for items in reader:
            if items:
                if int(items[0]) == int(id):
                    encontrado = True
                else:
                    arregloVacio.append(items)
                
    if encontrado:
        with open(ARCHIVO, 'w', newline = '', encoding = 'utf-8') as archivo_para_modificar:
            writer = csv.writer(archivo_para_modificar)
            writer.writerows(arregloVacio)
            return True
        
    else:
        return False
                
#‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾#
def ordenarPrecios():
    listaGastos = searhList()
    listaOrdenadaTemporalmente = []
    
    for items in listaGastos:
        listaOrdenadaTemporalmente.append([
            float(items[2]),
            items[0],
            items[1],
            items[3],
            items[4]])
        
    listaOrdenadaTemporalmente.sort()
    listaDefinitiva = []
    
    for items in listaOrdenadaTemporalmente:
        listaDefinitiva.append([
            items[1],
            items[2],
            items[0],
            items[3],
            items[4]])
    
    return listaDefinitiva
    
def ordenarPreciosMayor():
    lista = searhList()
    listaOrdenada = []
    
    for items in lista:
        listaOrdenada.append([
            float(items[2]),
            items[0],
            items[1],
            items[3],
            items[4]])
        
        listaOrdenada.sort(reverse=True)
        listaDefinitiva = []
        
        for items in listaOrdenada:
            listaDefinitiva.append([
                items[1],
                items[2],
                items[0],
                items[3],
                items[4]])
    return listaDefinitiva
                        
    
    
    
    
                    
#‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾#
    
    
