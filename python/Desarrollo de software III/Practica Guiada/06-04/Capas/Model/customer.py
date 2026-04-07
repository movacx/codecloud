class Customer:
    '''
    Entidad del dominio que representa el cliente
    Constructor de la clase, recibe el identificador el nombre y el telefono del cliente
    '''

    def __init__(self, identifier: str, name:str, phone:str):
        self.identifier = identifier 
        self.name = name
        self.phone = phone

    
    '''
    Convierte el objeto en un diccionario Esto es util para guardarlo en un Json
    '''

    def to_dict(self)->dict:
        return {
            'identifier': self.identifier,
            'name': self.name,
            'phone': self.phone

        }
    #Permite reconstruir un objeto cliente, a partir de un diccionario leido desde un JSON

    @classmethod
    def from_dict(cls, data:dict):
        return cls(
            data['identifier'],
            data['name'],
            data['phone']
        )
    
    'Define como se mostrara el objeto cuando se imprime'
    def __str__(self)->str:
        return f'Id: {self.identifier} | Nombre: {self.name} | Telefono: {self.phone}' 
        