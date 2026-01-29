import csv

from model.estudianteModel import Estudiante

dir_data= os.path.dirname(__file__)
ARCHIVO=os.path.join(dir_data,"csv","RegistrosEstudiantes.csv")

def validarUltimoId():
    if not os.path.exists(ARCHIVO):
        return 0
    ultimoId=0
    
    with open(ARCHIVO, "r",newline="",encoding="utf-8")as archivoParaLeer:
        reader=csv.reader(archivoParaLeer)
        for items in reader:
            if int (items[0])>ultimoId:
                ultimoId= int(items[0])
    return ultimoId