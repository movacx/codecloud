import os
import json
from Model.periferico import Periferico

dir_data = os.path.dirname(os.path.abspath(__file__))
Archivo = os.path.abspath(os.path.join(dir_data, '..','..','Data','perifericos.json'))

class Repositorio:
    def __init__(self):
        self.perifericos = []
        self._load()

#=====================================================================================
    def _load(self):
        if not os.path.exists(Archivo):
            return

        with open(Archivo, 'r', encoding='utf-8') as file:
            data = json.load(file)

            for items in data:
                nuevo_periferico = Periferico(
                    items['Modelo'],
                    items['Tipo'],
                    items['Precio']
                )

                self.perifericos.append(nuevo_periferico)

#=====================================================================================
    def _save(self):
        os.makedirs(os.path.dirname(Archivo), exist_ok=True)
        datos_para_guardar = []

        for items in self.perifericos:
            diccionario = items.to_dict()
            datos_para_guardar.append(diccionario)

        with open(Archivo, 'w', encoding='utf-8') as file:
            json.dump(datos_para_guardar, file, indent=4, ensure_ascii=False)

#=====================================================================================
    def agregar(self, objeto):
        self.perifericos.append(objeto)
        self._save()

#=====================================================================================
    def obtener_todos(self):
        return self.perifericos

#=====================================================================================
    def buscar_por_modelo(self, nombre_modelo):
        resultado = []
        for items in self.perifericos:
            if nombre_modelo.lower() in items.modelo.lower():
                resultado.append(items)
        return resultado



