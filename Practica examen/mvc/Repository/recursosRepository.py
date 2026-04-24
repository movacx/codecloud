import json, os

dir_data = os.path.dirname(os.path.abspath(__file__))
archivo = os.path.abspath(os.path.join(dir_data, '..','..','data','recursos.json'))

from Model.recursoModel import Recurso

class RecursosRepository:
    def __init__(self):
        self.lista_repositorios = []
        self._load()

    def _load(self):
        if not os.path.exists(archivo):
            return

        with open(archivo, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for items in data:
                nuevo_recurso = Recurso(items['codigoRecurso'], items['nombre'], items['categoria'], items['cantidadDisponible'], items['costoUnitario'])

                self.lista_repositorios.append(nuevo_recurso)

    def _save(self):s