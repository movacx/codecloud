import os
import sys
import csv
from datetime import datetime


dir_base = os.path.dirname(os.path.abspath(__file__))
fileUsuarios = os.path.abspath(os.path.join(dir_base, 'csv', 'registroUsuarios.csv'))
fileLogs = os.path.abspath(os.path.join(dir_base, 'logs', 'logfile.txt'))


class UsuarioBase:
    def __init__(self):
        pass
#--------------------------------------------------------------------------------------------------------------------------------
    def saveError(self, nombre_error):
        tiempo = datetime.now().strftime('%d%m%Y %H:%M:%S')
        try:
            
            with open(fileLogs, 'a', encoding = 'utf-8') as file:
                file.write(f'{tiempo}: {nombre_error}')

        except Exception as error:
            print(f'ERROR CRITICO FALLO EL [saveError].txt| {tiempo}, {error}')

#--------------------------------------------------------------------------------------------------------------------------------
    def addUsr(self, objetoModel):#Incompleto falta UltimoID
        try:
  
            with open(fileUsuarios, 'a', newline = '', encoding = 'utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(objetoModel.importar())
                return True

        except Exception as error:
            self.saveError(f' Error al intentar añadir: {error}')
            return None

#--------------------------------------------------------------------------------------------------------------------------------
    def list(self):
        try:
            if not os.path.exists(fileUsuarios):
                return []
            
            copyList = []

            with open(fileUsuarios, 'r', newline = '', encoding = 'utf-8') as file:
                reader = csv.reader(file)

                for lista in reader:
                    if lista:
                        copyList.append(lista)

            return copyList

        except Exception as error:
            self.saveError(f'Error al intentar Listar: {error}')
            return None
        
#--------------------------------------------------------------------------------------------------------------------------------
    def VerifyLogin(self, nombre, contraseña):
        try:
            
            if not os.path.exists(fileUsuarios):
                return []
            
            coincidencia = False

            with open(fileUsuarios, 'r', newline = '', encoding = 'utf-8') as file:
                reader = csv.reader(file)

                for lista in reader:
                    if lista:
                        if lista[1] == str(nombre):
                            if lista[2] == str(contraseña):
                                coincidencia = True
                                break
                                
            return coincidencia

        except Exception as error:
            self.saveError(f'Error al intentar Validar Login: {error}')
            return None