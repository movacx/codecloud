import os
import csv

dirData = os.path.dirname(os.path.abspath(__file__))
ARCHIVO = os.path.join(dirData, "csv", "resenas.csv")
#Leer reseñar
def leerResenas():
    try:
        if not os.path.exists(ARCHIVO): return []
        lista = [ ]
        
        with open(ARCHIVO, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            
            for items in reader:
                if items: 
                    lista.append(items)
        return lista
    
    except Exception as error:
        print(f"Error leer resenas: {error}")
        return [ ]
#-----------------------------------------------------------------------------------------------------------------------
#Guardar reseña 
def guardarResena(objResena):
    try:
		
        with open(ARCHIVO, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(objResena.importarToCsv())
            
        return True
    
    except Exception as error:
        print(f"Error guardar resena: {error}")
        return False
    