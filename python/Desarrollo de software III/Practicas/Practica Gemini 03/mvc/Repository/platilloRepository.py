import os
import json
from os.path import exists

dir_data = os.path.dirname(os.path.abspath(__file__))
Archivo = os.path.abspath(os.path.join(dir_data, '..', '..', 'Data', 'platillos.json'))

from Model.platilloModel import Platillo

class Repository:
    def __init__(self):
        self.listaPlatillos = []
        self._load()

    def _load(self):
        if not os.path.exists(Archivo):
            return

        with open(Archivo, 'r', encoding='utf-8') as file:
            data = json.load(file)

            for items in data:
                nuevo_platillo = Platillo(items['Nombre'], items['Precio'], items['Categoria'])

                self.listaPlatillos.append(nuevo_platillo)


    def _save(self):
        os.makedirs(os.path.dirname(Archivo), exist_ok=True)
        datos_para_guardar = []
        for items in self.listaPlatillos:
            diccionario = items.to_dict()
            datos_para_guardar.append(diccionario)

        with open(Archivo, 'w', encoding='utf-8') as file:
            json.dump(datos_para_guardar, file, indent=4, ensure_ascii=False)

    def agregar(self, objeto):
        self.listaPlatillos.append(objeto)
        self._save()

    def cargar_todos(self):
        return self.listaPlatillos

    def buscar_por(self, nombre):
        resultado = []
        for items in self.listaPlatillos:
            if nombre.lower() in items.nombre.lower():
                resultado.append(items)

        return resultado