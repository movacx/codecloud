class Platillo:
    def __init__(self, nombre:str, precio:float,categoria:str) -> None:
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def to_dict(self) -> dict:
        return {
            'Nombre': self.nombre,
            'Precio': self.precio,
            'Categoria': self.categoria
        }

    def __str__(self) -> str:
        return f'Nombre: {self.nombre}, Precio: {self.precio} Categoria: {self.categoria}'
