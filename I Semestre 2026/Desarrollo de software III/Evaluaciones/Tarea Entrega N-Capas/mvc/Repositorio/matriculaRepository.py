import os
import json

dir_data = os.path.dirname(os.path.abspath(__file__))
file_matricula = os.path.abspath(os.path.join(dir_data, '..','..','data','matricula.json'))

from Model.matricula import Matricula

class MatriculaRepository:
    def __init__(self):
        self.lista_matricula = []
        self._load()

    def _load(self):
        if not os.path.exists(file_matricula):
            return

        with open(file_matricula, 'r', encoding='utf-8') as file:
            data = json.load(file)

            for items in data:
                nueva_matricula = Matricula(items['Codigo matricula'], items['Carnet estudiante'], items['Codigo curso'], items['Periodo academico'])
                self.lista_matricula.append(nueva_matricula)

    def _save(self):
        os.makedirs(os.path.dirname(file_matricula), exist_ok=True)
        datos_para_guardar = []

        for items in self.lista_matricula:
            diccionario = items.to_dict()
            datos_para_guardar.append(diccionario)

        with open(file_matricula, 'w', encoding='utf-8') as file:
            json.dump(datos_para_guardar, file, indent=4, ensure_ascii=False)
            return True

    def agregar(self, objeto):
        self.lista_matricula.append(objeto)
        return self._save()

    def mostrar_matriculas(self):
        return self.lista_matricula

    def buscar_matricula(self, codigo_matricula):
        resultado = []

        for items in self.lista_matricula:
            if codigo_matricula.lower() ==  items.codigo_matricula.lower():
                resultado.append(items)

        return resultado


