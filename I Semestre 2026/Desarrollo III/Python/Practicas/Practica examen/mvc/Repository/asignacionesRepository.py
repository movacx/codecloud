
import json
import os

dir_data = os.path.dirname(os.path.abspath(__file__))
archivo = os.path.abspath(os.path.join(dir_data, '..','..','data','asignaciones.json'))

from Model.asignacionesModel import Asignaciones


class AsignacionesRepository:
    def __init__(self) -> None:
        self.listaAsignaciones = []
        self._load()

    def _load(self) -> None:
        if not os.path.exists(archivo):
            return

        with open(archivo, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for items in data:
                nueva_asignacion = Asignaciones(items['Codigo'], items['Beneficiario'], items['Recurso'], items['Cantidad entregada'], items['Fecha'], items['Responsable entrega'])

                self.listaAsignaciones.append(nueva_asignacion)

    def _save(self) -> bool:
        os.makedirs(os.path.dirname(archivo), exist_ok=True)
        datoParaGuardar = []

        for items in self.listaAsignaciones:
            diccionario = items.to_dict()
            datoParaGuardar.append(diccionario)

        with open(archivo, 'w', encoding='utf-8') as file:
            json.dump(datoParaGuardar, file, indent=4, ensure_ascii=False)
            return True

    def guardar(self, objeto) -> bool:
        self.listaAsignaciones.append(objeto)
        return self._save()

    def listar(self) -> list[Asignaciones]:
        return self.listaAsignaciones

    def buscar_asignacion(self, codigoAsignacion) -> list[Asignaciones]:
        resultado = []
        for items in self.listaAsignaciones:
            if codigoAsignacion.lower() == items.codigoAsignacion.lower():
                resultado.append(items)

        return resultado

