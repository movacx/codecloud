import os
import sys
import json

from Model.customer import Customer

class CustomerRepository:
    '''
    Repositorio de clientes
    SRP: Solo administra la persistencia y consulta de clientes
    '''

    #El repositorio recibe el nombre del archivo donde se guardan los clientes, Tambien prepara un alista y un dicionario para manejar los datos en memoria

    def __init__(self, filename = 'customer.json'):
        self._customers = []

        #Diccionario auxiliar par abuscar clientes rapidamente por identificador

        self._customers_by_id = {}

        #Se cargan los datos desde el archivo JSON, si existe
        #self._load()

        #Este metodo privado
        pass

    def _load(self):
        if not os.path.exists(self.filename):
            pass
        
        with open(self.filename, 'r', encoding = 'utf-8') as file:
            data = json.load(file)

            for item in data:
                customer = Customer.from_dict(item)

                self._customers.append(customer)
                self._customers_by_id[customer.identifier] = customer
                


    #Metodo privado que guarda los clientes actuales en el archivo JSON

    def _save(self):
        data = [Customer.to_dict() for customer in self._customers]
        #Se converte cada objeto customer en diccionario
        pass
    #Agrega un nuevo cliente al repositorio

