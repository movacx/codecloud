import os, sys
import csv
from datetime import datetime

dir_data = os.path.dirname(os.path.abspath(__file__))
ARCHIVO = os.path.abspath(os.path.join(dir_data, 'csv', 'historial.csv'))
LOG = os.path.abspath(os.path.join(dir_data, 'Logs', 'log.csv'))

class Data:
    def __init__(self):
        pass

    
    def reportLogs(self, nombreError):
        tiempo = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        try:

            
            with open(LOG, 'a', encoding = 'utf-8') as error_file:
                error_file.write(f'{tiempo}, {nombreError}\n')
        
        except Exception as error:
            print(f'{tiempo}, Error Critico! {error}')

        
    def registrarHistorial(self, objetoCalculadora):
        try:

            with open(ARCHIVO, 'a', newline = '', encoding = 'utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(objetoCalculadora.importar())
                return True
            
        except Exception as error:
            self.reportLogs(error)

        
    def mostrarHistorial(self):
        try:
            if not os.path.exists(ARCHIVO):
                return []
            
            arreglo = []

            with open(ARCHIVO, 'r', newline = '', encoding = 'utf-8') as file:
                reader = csv.reader(file)

                for lista in reader:
                    if lista:
                        arreglo.append(lista)

            return arreglo

        except Exception as error:
            self.reportLogs(error)

        


if __name__ == '__main__':
    print('Hola mundo')
