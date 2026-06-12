import os
import json

dir_data = os.path.dirname(os.path.abspath(__file__))
file_estudiante = os.path.abspath(os.path.join(dir_data, '..','..','data','estudiante.json'))

from Model.estudianteModel import Estudiante

class EstudianteRepository:
    def __init__(self):
        self.lista_estudiantes = []
        self._load()

# ========================================================================================================
    def _load(self):
        if not os.path.exists(file_estudiante):
            return

        with open(file_estudiante, 'r', encoding='utf-8') as file:
            data = json.load(file)

            for items in data:
                nuevo_estudiante = Estudiante(items['Carnet'], items['Nombre'], items['Carrera'])
                self.lista_estudiantes.append(nuevo_estudiante)

# =======================================================================================================
    def _save(self):
        os.makedirs(os.path.dirname(file_estudiante), exist_ok=True)
        datos_para_guardar = []

        for items in self.lista_estudiantes:
            diccionario = items.to_dict()
            datos_para_guardar.append(diccionario)

        with open(file_estudiante, 'w', encoding='utf-8') as file:
            json.dump(datos_para_guardar, file, indent=4, ensure_ascii=False)
            return True

    # =======================================================================================================
    def agregar(self, objeto):
        self.lista_estudiantes.append(objeto)
        return self._save()

    def mostrar_todo(self):
        return self.lista_estudiantes

    def buscar_estudiante(self, carnet):
        resultado = []

        for items in self.lista_estudiantes:
            if carnet.lower() == items.carnet.lower():
                resultado.append(items)
        return resultado