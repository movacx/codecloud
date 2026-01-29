import os
import sys
import csv

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
                ultimoId=items[0]
    return ultimoId

def registrarListado(objetoGasto):
    ultimoId=validarUltimoId()
    nuevoId=ultimoId+1
    with open(ARCHIVO,"a",newline="",encoding="utf-8")as nuevoRegistro:
        writer=csv.writer(nuevoRegistro)
        writer.writerow(objetoGasto.importToCsv())
                
    
    