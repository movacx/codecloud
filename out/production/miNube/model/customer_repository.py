import json
import os

from model.customer import Customer


class CustomerRepository:
    """
    Repositorio de clientes
    SRP: Solo administra la persistencia y consulta
    """
    #El repositorio recibe el nombre del archivo donde se guardan los clientes
    #Tambien prepara una lista y un diccionario para
    #manejar los datos en memoria

    def __init__(self, filename = "customer.json"):
        self.filename = filename

        #lista con todos los clientes
        self._customers=[]

        #diccionario auxiliar para buscar clientes rapidamente
        #por identificador

        self._customers_by_id={}

        #se cargan los datos desde el archivo JSON, si existe
        # self._load() #an no existe

        #Este metodo privado carga los clientes desde el archivo

    def _load(self):
        #si el archivo toda no exite, no hay nada que cargar
        if not os.path.exists(self.filename):
            return
        #se abre el archivo en modo lectura
        #se transforma su contenido JSON en clientes

        with open(self.filename, "r", encoding="utf-8") as file:
            data=json.load(file)

        #casa elemento leido del archivo se convierte
        #en un obejto Customer
        for item in data:
            customer=Customer.from_dict(item)

            # se guarda en la lista y en el diccionario
            self._customers.append(customer)
            self._customers_by_id[customer.identifier] = customer


    #metodo privado que guarda los clientes actuales
    #en el archivo JSON


    def _save(self):
        # se convierte cada objeto Customer en diccionario
        data = [customer.to_dict() for customer in self._customers]

        #se sobreescribe el archivo con la lista actual de clientes
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    #agregar un nuevo cliente al repositorio
    def add (self, customer:Customer):
        # se verifica que no exista otro cliente con el mismo id
        if customer.identifier in self._customers_by_id:
            raise ValueError ("Ya existe el cliente")
        #Se guarda en la lista y en el diccionario
        self._customers.append(customer)
        self._customers_by_id[customer.identifier] = customer

        #se guardan los datos en el archivo
        self._save()

    #busca un cliente por identificador, si no existe retorna None
    def get_by__id(self, identifier:str):
        return self._customers_by_id.get(identifier)
    #devuelve una copia de la lista de los clientes
    #usa list para presentar la lista entera
    def get_all(self):
        return list(self._customers)
    #retorna True o False, dependiendo de si existe o no
    #un cliente con ese id
    def exists(self, identifier:str)->bool:
        return identifier in self._customers_by_id
























