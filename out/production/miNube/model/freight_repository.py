import json
import os.path

from model.freight import Freight


class FreightRepository:
    """
    Este repositorio gestiona la persistencia de los fletes
    SRP: Solo administra persistencia y consultas de fletes
    """
    #El repositorio recibe el nombre del archivo
    #donde se guardarán los fletes

    def __init__(self, filename= "freights.json"):
        self.filename = filename


        #lista con todos los fletes registrados
        self._freights = []

        #diccionario que agrupa fletes por identificador de cliente
        #La llave es customer_id y el valor es una lista de fletes

        #dieccioanrio tiene una llave y un valor asociado, en este caso el valor asociado es una lista vacia
        self._freights_by_customer_id = {}
        #se intenta cargar la informacion ya guardada


    #Carga los fletes desde el archivo JSON
    def _load (self):
        #si no existe este archivo no se retorna nd
        if not(os.path.isfile(self.filename)):
            return
        #si existe abra este with y lo abre de modo lectura (escritura), esta codificado en utf-8
        with open(self.filename, "r" , encoding = "utf-8") as file:
            #declara variable para que cargue del archivo json file
            data= json.load(file)
        # tomamos cada item que existe y lo que hacemos es ver el (metodo de la clase flete) que convierte de diccionario a flete
        for item in data:
            #definimos flete, para que convierta de un diccionario ese item para que nos devuelva un flete
            freight = Freight.from_dict(item)
            #una lista que agrega un flete a la lista
            self._freights.append(freight)
            #si no existe una lista para este cliente, la crea
            #esto es un diccionario self._freights_by_customer_id:
            if freight.customer_id not in self._freights_by_customer_id:
                #creamos para ese cliente una lista vacía
                self._freights_by_customer_id[freight.customer_id] = []
            #luego se agrega el flete a la lista del cliente correspondiente
            self._freights_by_customer_id[freight.customer_id].append(freight)
    #Guarda en el archivo los fletes
    def _save(self):

        #data = pasa de dicconario los fletes que tengan en la lista de fletes
        data = [freight.to_dict() for freight in self._freights]
        #se abre no como escritura si no como lectura
        with open(self.filename, "w" , encoding = "utf-8") as file:
            #mete toda la data dentro del archivo flete.json
            json.dump(data, file, indent = 4, ensure_ascii=False)

    #agrega un flete nuevo al repositorio
    def add(self, freight: Freight):
        #agregamos el nuevo flete en la lista de flete
        self._freights.append(freight)
        #si el id del cliente no esta en el dicconario
        if freight.customer_id not in self._freights_by_customer_id:
            #se crea la lista
            self._freights_by_customer_id[freight.customer_id] = []
        #si si, se agrega a la lista dentro del dccionario
        self._freights_by_customer_id[freight.customer_id].append(freight)
        self._save()

    #Devuelve todos los fletes
    def get_all(self):
        return list(self._freights)

    #Devuelve todos los fletes asociados a un cliente en especifico
    def get_by_customer_id(self, customer_id:str):
        return list(self._freights_by_customer_id.get(customer_id))




