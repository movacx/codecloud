import os
import sys
import csv

dir_data = os.path.dirname(os.path.abspath(__file__))
ARCHIVO = os.path.join(dir_data,'csv','registroChanca.csv')

#‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
def verificarUltimoId():
    ultimoId = 0
    
    with open(ARCHIVO,'r',newline='',encoding='utf-8') as archivo_para_leer:
        reader = csv.reader(archivo_para_leer)
        
        for lista in reader:
            if lista:
                if int(lista[0] > ultimoId):
                    ultimoId = int(lista[0])
    return ultimoId

#‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾

def addList(objeto_cancha):
    with open(ARCHIVO, 'a', newline='',encoding='utf-8') as add_file:
        writer = csv.writer(add_file)
        writer.writerow(objeto_cancha.importTocsv())
    return True

#‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾

def searchList():
    lista = []
    
    with open(ARCHIVO,'r',newline='',encoding='utf-8') as archivo_para_copiar:
        reader = csv.reader(archivo_para_copiar)
        
        for items in reader:
            lista.append(items)
            
    return lista

#‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
        
        
        
    
    
    
    
            
            
    