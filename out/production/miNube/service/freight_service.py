from model import customer_repository
from model.customer import Customer


class FreightService:
    """
    Capa lógica de negocio
    SRP: Contiene las reglas del sistema
    DIP: recibe repositorios por inyeccion

    """
    #El servicio recibe los repositorios desde afuera
    #esto permite separra la logica de negocio del acceso a los datos
    def __init__(self, customer_repositoriy, freight_repository):
        self.customer_repository = customer_repository
        self.freight_repository = freight_repository

    #registra un cliente nuevo validando primero sus datos
    def register_customer(self, identifier:str, name:str, phone:str):
        if not identifier.strip():
            raise ValueError ("El identificador no puede estar vacio")
        if not name.strip():
            raise ValueError ("El nombre no puede estar vacio")
        if not phone.strip():
            raise ValueError ("El numero no puede estar vacio")

        #si los datos son validos, se construye el cliente
        customer= Customer(identifier, name, phone)

        #se almacena en el repositorio
        self.customer_repository.add(customer)

    #registrar un flete

    def register_freight(self, number:str, amount:float, customer_id:str, origin:str, destination:str, weight:float):
        #validaciones de negocio
        if not number.strip():
            raise ValueError ("El numero no puede estar vacio")
        if amount <= 0:
            raise ValueError ("El numero no puede estar vacio")
        if not customer_id.strip():
            raise ValueError ("El numero de cliente no puede estar vacio")
        if not origin.strip():
            raise ValueError ("El origen no puede estar vacio")
        if not destination.strip():
            raise ValueError ("El destino no puede estar vacio")
        if weight <= 0:
            raise ValueError ("El peso no puede estar vacio")

        #se verifica que el cliente exista antes de registrar el flete
        customer= self.customer_repository.get_by_id(customer_id)
        if customer is None:
            raise ValueError ("El cliente no existe")
        #la ruta se modela como una tupla: (origen:Destino)
        route=(origin,destination)

        #regla de negocio para calcular el monto
        amount= weight*1500

        #se crea y se guardan l

