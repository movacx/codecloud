import json, os

dir_data = os.path.dirname(os.path.abspath(__file__))
archivo = os.path.abspath(os.path.join(dir_data, '..','..','data','recursos.json'))

from Model.recursoModel import Recurso

class RecursosRepository:
    def __init__(self):
        self.lista_recursos = []
        self._load()

    def _load(self):
        if not os.path.exists(archivo):
            return

        with open(archivo, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for items in data:
                nuevo_recurso = Recurso(items['codigoRecurso'], items['nombre'], items['categoria'], items['cantidadDisponible'], items['costoUnitario'])

                self.lista_recursos.append(nuevo_recurso)

    def _save(self):
        os.makedirs(os.path.dirname(archivo), exist_ok=True)
        dato_para_guardar = []

        for items in self.lista_recursos:
            diccionario = items.to_dict()
            dato_para_guardar.append(diccionario)

        with open(archivo, 'w', encoding='utf-8') as file:
            json.dump(dato_para_guardar, file, indent=4, ensure_ascii=False)
            return True

    def guardar(self, objeto):
        self.lista_recursos.append(objeto)
        return self._save()

    def listar(self):
        return self.lista_recursos

    def buscar_recurso(self, codigo):
        resultado = []
        for items in self.lista_recursos:
            if codigo.lower() == items.codigoRecurso.lower():
                resultado.append(items)
        return resultado
