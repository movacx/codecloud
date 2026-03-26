class Libro:
    def __init__(self, codigoLibro, titulo, autor, categoria):
        self.codigoLibro = codigoLibro
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria

    def __str__(self):
        return  f"""
Codigo: {self.codigoLibro}
Titulo: {self.titulo}
Autor: {self.autor}
Categoria: {self.categoria}"""