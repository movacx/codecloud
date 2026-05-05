import json
import os

dir_data = os.path.dirname(os.path.abspath(__file__))
archivo = os.path.abspath(os.path.join(dir_data, '..','..','data','personas.json'))

from Model.personaBeneficiariaModel import Beneficiaria


class PersonaRepository:
    def __init__(self)->None:
        self.listaPersonasBeneficiarias = []
        self._load()

    def _load(self):
        if not os.path.exists(archivo):
            return

        with open(archivo, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for items in data:
                nuevoBeneficiario = Beneficiaria(items['Cedula'], items['Nombre'], items['Comunidad'], items['Cantidad Integrantes'], items['Prioridad Social'])

                self.listaPersonasBeneficiarias.append(nuevoBeneficiario)

    def _save(self)->bool:
        os.makedirs(os.path.dirname(archivo), exist_ok=True)
        datoParaGuardar = []

        for items in self.listaPersonasBeneficiarias:
            diccionario = items.to_dict()
            datoParaGuardar.append(diccionario)

        with open(archivo, 'w', encoding='utf-8') as file:
            json.dump(datoParaGuardar, file, indent=4, ensure_ascii=False)
            return True

    def guardar(self, objeto)->bool:
        self.listaPersonasBeneficiarias.append(objeto)
        return self._save()

    def listar(self)->list[Beneficiaria]:
        return self.listaPersonasBeneficiarias

    def buscarBeneficiario(self, id)->list[Beneficiaria]:
        resultado = []
        for items in self.listaPersonasBeneficiarias:
            if id.lower() == items.id.lower():
                resultado.append(items)

        return resultado



