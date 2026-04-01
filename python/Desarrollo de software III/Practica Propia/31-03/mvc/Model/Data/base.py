import os, sys
import csv

dirData = os.path.dirname(os.path.abspath(__file__))
Archivo = os.path.abspath(os.path.join(dirData, 'csv', 'registroEstudiante.csv'))



class BaseEstudiantes:

    #==================================================================================================================#
    def validarUltimoId(self):
        if not os.path.exists(Archivo):
            return 0
        
        ultimoId = 0
        
        with open(Archivo, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            
            for lista in reader:
                if lista:
                    id_actual = int(lista[0])
                    if id_actual > ultimoId:
                        ultimoId = id_actual
                        
        return ultimoId
    

    #==================================================================================================================#
    def registrar(self, objeto):
    
        ulId = self.validarUltimoId()
        ultimoId = ulId + 1

        objeto.setId(ultimoId)
        

        with open(Archivo, 'a', newline = '', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(objeto.exportar())
            return True


    #==================================================================================================================#
    def listar(self):
        if not os.path.exists(Archivo):
            return []
        
        lista = []

        with open(Archivo, 'r', newline = '', encoding='utf-8') as file:
            reader = csv.reader(file)

            for items in reader:
                lista.append(items)

            return lista
    #==================================================================================================================#