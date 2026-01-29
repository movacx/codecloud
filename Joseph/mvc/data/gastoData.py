import os
import sys
import csv

from model.gastosModel import GastoModel

dir_data= os.path.dirname(__file__)#MVC/DATA/gastoData.py
ARCHIVO=os.path.join(dir_data,"csv","RegistroGasto.csv")
#dir_data/csv/registroGasto.csv
def validarUltimoId():
    if not os.path.exists(ARCHIVO):
        return 0
    
    ultimoId=0
    with open(ARCHIVO,"r",newline="",encoding="utf-8")as archivoParaLeer:
        reader=csv.reader(archivoParaLeer)
        for items in reader:
            if int(items[0])> ultimoId:
                ultimoId=int(items[0])
    return ultimoId

def registrarListado(objetoGasto):
    ultimoId=validarUltimoId()
    nuevoId=ultimoId+1
    objetoGasto.setId(nuevoId)
    with open(ARCHIVO,"a",newline="",encoding="utf-8")as nuevoRegistro:
        writer=csv.writer(nuevoRegistro)
        writer.writerow(objetoGasto.importToCsv())
                
def listarTodos():
    arregloVacio=[]
    with open(ARCHIVO, "r", newline="",encoding="utf-8")as archivoParaLeer:
        reader=csv.reader(archivoParaLeer)
        for items in reader:
            arregloVacio.append(items)
    return arregloVacio

def eliminarGasto(id):
    arregloVacio=[]
    bloqueo=True
    with open(ARCHIVO, "r", newline="",encoding="utf-8")as archivoParaLeer:
        reader=csv.reader(archivoParaLeer)
        for items in reader:
            if int(items[0])!=int(id):
                arregloVacio.append(items)
                bloqueo = False
                
    if bloqueo == True:
        return True
    else:
        with open(ARCHIVO, "w", newline="", encoding="utf-8")as archivoParaModificar:
            writer=csv.writer(archivoParaModificar)
            writer.writerows(arregloVacio)
            return False
                
                