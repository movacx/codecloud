class Videojuego:
    def __init__(self, titulo, genero, precio):
        self.titulo = titulo
        self.genero = genero
        self.precio = precio

    def to_dict(self):
        #Retornamos los datos como un diccionario simple
        return {
            'titulo': self.titulo,
            'genero': self.genero,
            'precio':self.precio
        }

    