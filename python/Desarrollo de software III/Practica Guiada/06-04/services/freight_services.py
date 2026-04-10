from Model.customer import Customer

class FreightService:
    '''
    Capa logica del negocio
    SRP: CONTIENE LAS REGLAS DEL SISTEMA
    DIP: recibe repositorios por inyeccion
    '''

    #El servicio recibe los repositorios desde afuera.
    # Esto permite separar

    def __init__(self, customer_repository, freight_repository):
        self.customer_Repository = customer_repository
        self.freight_repository = freight_repository

    #Registra un cliente nuevo validando primero sus datos
    def register_customer(self, identifier:str, name: str,phone:str):
        if not identifier.strip():
            raise ValueError('El identificador no puede estar vacio')
        
        if not name.strip():
            raise ValueError('El nombre no puede estar vacio')
        if not phone.strip():
            raise ValueError('El telefono no puede estar vacio')
        
        customer = Customer(identifier, name, phone)

        self.customer_Repository.add(customer)

    #Registrar un flete
    def register_freight(self, number:str, amount:float, customer_id:str, origin:str, destination:str, weight:float):
        if not number.strip():
            raise ValueError('El numero de flete no puede estar vacio')
        if amount <= 0:
            raise ValueError('La cantidad no pede ser menor que 0')
        if not customer_id.strip():
            raise ValueError('El numero de cliente no puede estar vacio')
        if not origin.strip():
            raise ValueError('El destino no puede estar vacio')
        if weight <=0:
            raise ValueError('El peso no puede ser menor a cero')
        
        #Se verifica qe el cliente exista antes de registrar el flete
        customer = self.customer_Repository.get_by_id(customer_id)


        if customer is None:
            raise ValueError('eL CIENTE NO EXISTE')