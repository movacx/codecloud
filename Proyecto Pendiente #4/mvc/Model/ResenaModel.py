class ResenaModel:
    def __init__(self, idProducto, idUsuario, comentario, estrellas):
        self.idProducto = idProducto
        self.idUsuario = idUsuario
        self.comentario = comentario
        self.estrellas = estrellas

    def importarToCsv(self):
        return [self.idProducto, self.idUsuario, self.comentario, self.estrellas]
