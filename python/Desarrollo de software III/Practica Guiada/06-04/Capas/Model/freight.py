class Freight:
    '''
    Entidad del dominio que representa un flete
    '''

    #Constructor del flete
    #route es una tupla que contiene el origen yy el destino

    def __init__(self, number:str, amount:float, customer_id, route: tuple, weight:float):
        self.number = number
        self.amount = amount
        self.customer_id = customer_id
        self.route = route
        self.weight = weight

    #Convierte el objeto Freight en un diccionario para guardarlo en JSON

    def to_dict(self):
        return {
            'number': self.number,
            'amount': self.amount,
            'customer_id': self.customer_id,
            'route': {
                'Origin': self.route[0],
                'Destination': self.route[1],                
            },
            'weight': self.weight

        }
    
    #Reconstruye un objeto Freight a partir de un diccionario
    @classmethod
    def from_dict(cls, data:dict):
        return cls(
            data['number'], 
            data['amount'], 
            data['customer_id'],
            (data['route']['origin'], data['route']['destination']), 
            data['weight'])