import os
import csv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVO = os.path.join(BASE_DIR, "csv", "resenas.csv")

def leerResenas():
    try:
        if not os.path.exists(ARCHIVO): return []
        lista = []
        with open(ARCHIVO, "r", newline="", encoding="utf-8") as file:
            lector = csv.reader(file)
            for fila in lector:
                if fila: lista.append(fila)
        return lista
    except Exception as e:
        print(f"Error leer resenas: {e}")
        return []

def guardarResena(objResena):
    try:
        with open(ARCHIVO, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(objResena.importarToCsv())
        return True
    except Exception as e:
        print(f"Error guardar resena: {e}")
        return False