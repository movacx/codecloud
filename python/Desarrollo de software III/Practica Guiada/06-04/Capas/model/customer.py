class Customer:

    """
    Entidad del dominio que representa al cliente
    """
    """
    Constructor de la clase, recibe el identificador
    el nombre y el telefono del cliente
    """

    def __init__(self, identifier: str, name:str, phone: str):
        self.identifier = identifier
        self.name = name
        self.phone = phone

    """
    convierte el objeto en un diccionario
    esto es util para guardarlo en un JSON
    
    objeto - diccionario
    """
    def to_dict(self) -> dict:
        return {
            "identifier" : self.identifier,
            "name" : self.name,
            "phone" : self.phone
        }
    """
    Permite construir un objeto cliente, 
    a partir de un diccionario leído desde JSON
    """
    """
    cls hace referencia a la clase que estamos manejando diccionario - objeto
    """
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            data["identifier"],
            data["name"],
            data["phone"]
        )
    
    #Define como se mostrará el objeto cuando se imprime

    def __str__(self) -> str:
        return f"ID: {self.identifier} Nombre: {self.name} Telefono: {self.phone}"

