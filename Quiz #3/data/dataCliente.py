import os
import sys
import csv
from datetime import datetime

sys.stdout.reconfigure(encoding="utf-8")

dir_name = os.path.dirname(os.path.abspath(__file__))
ARCHIVO = os.path.join(dir_name, 'csv', 'dataCliente.csv')
logFile = os.path.join(dir_name, 'log', 'logfile.txt')

def guardarError(errorTexto):
    try:
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        mensaje = f'(fecha) ===> {errorTexto}\n'
        
        with open(logFile, 'a', encoding='utf-8')as file:
            file.write(mensaje)
            
    except Exception as nombreError:
        print('Error critico en log: {nombreError}')
    