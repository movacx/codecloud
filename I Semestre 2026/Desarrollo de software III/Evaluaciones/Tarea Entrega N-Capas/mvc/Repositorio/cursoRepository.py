import os
import json

dir_data = os.path.dirname(os.path.abspath(__file__))
File_Curso = os.path.abspath(os.path.join(dir_data, '..','..','data','cursos.json'))

from Model.cursoModel import Curso

class CursoRepository:
    def __init__(self):
        self.lista_cursos = []
        self._load()

    #=============================================================================================
    def _load(self):
        if not os.path.exists(File_Curso):
            return

        with open(File_Curso, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for items in data:
                nuevo_curso = Curso(items['Codigo'], items['Curso'], items['Creditos'])

                self.lista_cursos.append(nuevo_curso)

    #=============================================================================================
    def _save(self):
        os.makedirs(os.path.dirname(File_Curso), exist_ok=True)
        dato_para_guardar = []

        for items in self.lista_cursos:
            diccionario = items.to_dict()
            dato_para_guardar.append(diccionario)

        with open(File_Curso, 'w', encoding='utf-8') as file:
            json.dump(dato_para_guardar, file, indent=4, ensure_ascii=False)
            return True

    #=============================================================================================
    def guardar(self, objeto):
        self.lista_cursos.append(objeto)
        return self._save()


    #=============================================================================================
    def obtener_todos(self):
        return self.lista_cursos

    #=============================================================================================
    def buscar_por_curso(self, codigo_curso):
        resultados = []
        for items in self.lista_cursos:
            if codigo_curso.lower() == items.codigo_curso.lower():
                resultados.append(items)
        return resultados
    #=============================================================================================


