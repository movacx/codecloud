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
    with open(ARCHIVO,newline="",encoding="utf-8")as archivoParaLeer:
        reader=csv.reader(archivoParaLeer)
    
    