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
        
        for item in reader:
            if int(item[0]) != int(id):
                arregloVacio.append(item)
                encontrado = True
                
    if encontrado:
        with open(ARCHIVO, 'w', newline = '', encoding = 'utf-8') as archivo_para_modificar:
            writer = csv.writer(archivo_para_modificar)
            writer.writerows(arregloVacio)
            return encontrado
        
    else:
        return encontrado
                
                
    
    
    
    
    
    
    
                    
#‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾#
    
    
