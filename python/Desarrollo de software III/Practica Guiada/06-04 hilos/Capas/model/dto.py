class FreightViewDTO:
    """
    presenta los datos del flete en la vista
    evita que el GUI tenga que reconstruir información compleja

    Este objeto no representa la entidad real del dominio
    si no, una versión simplificada para mostrar los datos
    en la interfaz
    """

    def __init__(self, number, customer_name, origin, destination, weight, amount):
        self.number = number
        self.customer_name = customer_name
        self.origin = origin
        self.destination = destination
        self.weight = weight
        self.amount = amount

