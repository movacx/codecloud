import sys
import os
import csv

from datetime import datetime
dir_data = os.path.dirname(os.path.abspath(__file__))
ARCHIVO = os.path.abspath(os.path.join(dir_data, 'csv', 'clientes.csv'))
LOGFILE = os.path.abspath(os.path.join(dir_data, 'log', 'filerror.txt'))

class DataClientes:
    def __init__(self):
        pass
    
    def savelog(self, error):
        tiempo = datetime.now().strftime('%d%m%Y %H:%M:%S')
        try:
            
            with open(LOGFILE, 'a', encoding = 'utf-8') as file:
                file.write(f'{tiempo}: Hubo un error, valide la clase DataClientes: {error}\n')
            return True
            
        except Exception as error_savelog:
            print(f'error critico! {error_savelog}')

#-----------------------------------------------------------------------------------------------------------------

    def saveCliente(self, objeto):
       try:
           
           with open(ARCHIVO, 'a', newline = '', encoding = 'utf-8') as file:
               writer = csv.writer(file)
               writer.writerow(objeto.exportar())
               return True
           
       except Exception as error:
           self.savelog(f'{error} in saveCliente')
           
           
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
                            self.savelog(f'{error} in [if listCliente]')
            return arreglo
        except Exception as error:
            self.savelog(f'{error} in listCliente')

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
                            self.savelog(f'{error} in [if searchCliente]')
            return arreglo
        except Exception as error:
            self.savelog(f'{error} in searchCliente')

#-----------------------------------------------------------------------------------------------------------------


    def deleteDNI(self, dni):
        encontrado = False
        listaExclusiva = []
        try:
            
            if not os.path.exists(ARCHIVO):
                return []
            
            with open(ARCHIVO, 'r', newline = '', encoding = 'utf-8') as file:
                reader = csv.reader(file)
                
                for items in reader:
                    if items:
                        try:
                            
                        
                            if str(items[0]).lower() == str(dni).lower():
                                encontrado = True
                            else:    
                                listaExclusiva.append(items)
                        
                        except Exception as error:
                            self.savelog(f'{error} in if delete')

                        
                            
            if encontrado == True:
                with open(ARCHIVO, 'w', newline = '', encoding = 'utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerows(listaExclusiva)
                return True
            else:
                return False
            
            
        except Exception as error:
            self.savelog(f'{error} in deleteDNI')

#-----------------------------------------------------------------------------------------------------------------

    def modificar(self, dni, nombre, apellido, email):
        encontrado = False
        arreglo = []
        try:
            if not os.path.exists(ARCHIVO):
                return False
            
            with open(ARCHIVO, 'r', newline = '', encoding = 'utf-8') as file:
                reader = csv.reader(file)
                for items in reader:
                    if items:
                        try:
                            if str(items[0]).lower() == str(dni).lower():
                                items[1] = nombre
                                items[2] = apellido
                                items[3] = email
                                arreglo.append(items)
                                encontrado = True 
                            else:
                                arreglo.append(items)
                        except Exception as error:
                            self.savelog(f'{error} in if modificar')
                            
            if encontrado == True:
                with open(ARCHIVO, 'w', newline = '', encoding = 'utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerows(arreglo)
                return True
            else:
                return False
                    
        except Exception as error:
            self.savelog(error)
            