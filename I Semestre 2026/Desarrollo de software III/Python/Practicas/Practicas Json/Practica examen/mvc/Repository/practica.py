import os
import json

dir_data = os.path.dirname(os.path.abspath(__file__))
archivo = os.path.abspath(os.path.join(dir_data, '..','..','data','prueba.json'))

from Model.libroModel import LibroModel


class ClasePrueba:
    def __init__(self):
        self.lista_libro = []
        self._load()

    #=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

    def _load(self):
        if not os.path.exists(archivo):
            return
        
        with open(archivo, 'r', encoding='utf-8') as file:
            data = json.load(file)

            for items in data:
                nuevo_libro = LibroModel(items['Id'],items['Nombre'],items['Autor'])

                self.lista_libro.append(nuevo_libro)

    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-#

    def _save(self):
        os.makedirs(os.path.dirname(archivo), exist_ok=True)
        datos_para_guardar = []

        for items in self.lista_libro:
            diccionario = items.to_dict()
            datos_para_guardar.append(diccionario)

        with open(archivo, 'w', encoding='utf-8') as file:
            json.dump(datos_para_guardar, file, indent=4, ensure_ascii=False)
            return True

    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=---=-==-=-=-=#

    def guardar(self, objeto):
        self.lista_libro.append(objeto)
        return self._save()

    def listar(self):
        return self.lista_libro
    
    def buscar_libro(self, ide):
        resultado = []
        for items in self.lista_libro:
            if ide.lower() == items.id.lower():
                resultado.append(items)
        
        return resultado