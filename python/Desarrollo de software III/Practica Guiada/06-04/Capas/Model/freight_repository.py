import os.path
import json
from Model.freight import Freight

class FreightRepository:
    '''
    Este repositorio gestiona la persistencia de los fletes
    SRP: Solo administra persistencia y consultas de fletes
    '''

    #El repositorio recibe el nombre del archivo donde se guardaran los fletes


    def __init__(self, filename = 'freights.json'):
        self.filename = filename
        
        #Lista con todos los fletes registrados
        self._freights=[]

        #Diccionario que agrupa fletes por identificador de cliente
        #La llave es customer_id y el valor es una lista de fletes

        self._freights_by_customer_id = {}

        #Se intenta cargar la informacion ya guardada
        #self._load() por el momento no existe

    def _load(self):
        if not os.path.exists(self.filename):
            return
        
        with open(self.filename, 'r', encoding='utf-8') as file:
            data = json.load(file)

            for item in data:
                freight = Freight.from_dict(item)
                self._freights.append(freight)

            #Si no existe una lista para ese cliente, la crea

            if freight.customer_id not in self._freights_by_customer_id:
                self._freights_by_customer_id[freight.customer_id]=[]

            #luego se agrega el flete a la lista del cliente correspondiente
            self._freights_by_customer_id[freight.customer_id].append(freight)

    #Guarda en el archivo los fletes atuales

    def _save(self):
        data = [Freight.to_dict() for freight in self._freights]

        with open(self.filename, 'w', encoding = 'utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    #agrega un flete nuevo al repositorio
    def add(self, freight: Freight):
        self._freights.append(freight)

        if freight.customer_id not in self._freights_by_customer_id:
            self._freights_by_customer_id[freight.customer_id] = []

        self._freights_by_customer_id[freight.customer_id].append(freight)
        self._save()

    #Devuelve todos los fletes

    def get_all(self):
        return list(self._freights)
    
    #devuelve todos los fletes asociados a un cliente especifico

    def get_by_customer_id(self, customer_id):
        pass
    