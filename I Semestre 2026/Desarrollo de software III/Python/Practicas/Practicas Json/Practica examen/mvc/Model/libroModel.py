class LibroModel:
    def __init__(self, id, nombre, autor):
        self.id = id
        self.nombre = nombre
        self.autor = autor

    def __str__(self):
        return f'{self.id}, {self.nombre}, {self.autor}'
        
    def to_dict(self):
        return {
            'Id':self.id,
            'Nombre':self.nombre,
            'Autor':self.autor
        }
    