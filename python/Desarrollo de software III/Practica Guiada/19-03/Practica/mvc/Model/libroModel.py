class Libro:
    def __init__(self, codigoLibro, titulo, autor, categoria):
        self.codigoLibro = codigoLibro
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria

    def __str__(self):
        return f"{self.codigoLibro} | {self.titulo} | {self.autor} | {self.categoria}"
