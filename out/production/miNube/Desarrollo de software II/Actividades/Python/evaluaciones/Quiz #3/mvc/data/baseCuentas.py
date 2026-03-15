import sys
import os
import csv

from datetime import datetime
dir_data = os.path.dirname(os.path.abspath(__file__))
ARCHIVO = os.path.abspath(os.path.join(dir_data, 'csv', 'cuentas.csv'))
LOGFILE = os.path.abspath(os.path.join(dir_data, 'log', 'filerror.txt'))

class DataCuentas:
    def __init__(self):
        pass
    
    def savelog(self, error):
        tiempo = datetime.now().strftime('%d%m%Y %:H%:M%:S')
        try:
            
            with open(LOGFILE, 'a', encoding = 'utf-8') as file:
                file.write(f'{tiempo}: Hubo un error, valide la clase DataCuentas!!!!: {error}\n')
            return True
            
        except Exception as error_savelog:
            print(f'error critico! {error_savelog}')

#-----------------------------------------------------------------------------------------------------------------

    def saveCuenta(self, objeto):
       try:
           
           with open(ARCHIVO, 'a', newline = '', encoding = 'utf-8') as file:
               writer = csv.writer(file)
               writer.writerow(objeto.exportar())
               return True
           
       except Exception as error:
           self.savelog(f'{error} in saveCuenta')
           
           
    def list(self):
        arreglo = []
        try:
            if not os.path.exists(ARCHIVO):
                return []
            with open(ARCHIVO, 'r', newline = '', encoding = 'utf-8') as file:
                reader = csv.reader(file)
                
                for items in reader:
                    if items:
                        try:
                            arreglo.append(items)
                        except Exception as error:
                            self.savelog(f'{error} in [if funcionList]')
            return arreglo
        except Exception as error:
            self.savelog(f'{error} in funcionList')

#-----------------------------------------------------------------------------------------------------------------
            
    def searchList(self, dni):
        arreglo = []
        try:
            if not os.path.exists(ARCHIVO):
                return []
            with open(ARCHIVO, 'r', newline = '', encoding = 'utf-8') as file:
                reader = csv.reader(file)
                
                for items in reader:
                    if str(items[0]).lower() == str(dni).lower():
                        try:
                            arreglo.append(items)
                        except Exception as error:
                            self.savelog(f'{error} in [if searchCuenta]')
            return arreglo
        except Exception as error:
            self.savelog(f'{error} in searchCuenta')
            
            
    def obtenerSaldo(self, numeroCuenta):
        arreglo = []
        try:
            if not os.path.exists(ARCHIVO):
                return []
            with open(ARCHIVO, 'r', newline = '', encoding = 'utf-8') as file:
                reader = csv.reader(file)
                
                for items in reader:
                    if str(items[1]).lower() == str(numeroCuenta).lower():
                        try:
                            arreglo.append(items)
                        except Exception as error:
                            self.savelog(f'{error} in [if searchCuenta]')
            return arreglo
        except Exception as error:
            self.savelog(f'{error} in searchCuenta')


#-----------------------------------------------------------------------------------------------------------------




    def modificar(self, cuenta, saldo):
        encontrado = False
        arreglo = []
        try:
            if not os.path.exists(ARCHIVO):
                return []
            
            with open(ARCHIVO, 'r', newline = '', encoding = 'utf-8') as file:
                reader = csv.reader(file)
                for items in reader:
                    if items:
                        try:
                            if str(items[1]).lower() == str(cuenta).lower():
                                items[2] = str(saldo)
                                arreglo.append(items)
                                encontrado = True 
                            else:
                                arreglo.append(items)
                        except Exception as error:
                            self.savelog(f'{error} in if modificar CUENTAS')
                            
            if encontrado == True:
                with open(ARCHIVO, 'w', newline = '', encoding = 'utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerows(arreglo)
                return True
            else:
                return False
                    
        except Exception as error:
            self.savelog(error)

#-----------------------------------------------------------------------------------------------------------------

    def ordenar(self):
        listaDesordenada = self.list()
        listaOrdenadaTemporal = []

        for items in listaDesordenada:
            listaOrdenadaTemporal.append((float(items[2]), items[0], items[1]))

        listaOrdenadaTemporal.sort(reverse= True)
        listaDefinitiva = []

        for items in listaOrdenadaTemporal:
            listaDefinitiva.append((items[1], items[2], items[0]))

        return listaDefinitiva
        
