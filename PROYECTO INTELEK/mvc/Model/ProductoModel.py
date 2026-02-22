class ProductoModel:
    def __init__(self, ide, nombre, categoria, precio, stock, socketCpu, tipoRam):
        self.ide = ide
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock
        self.socketCpu = socketCpu
        self.tipoRam = tipoRam

    def importarToCsv(self):
        return [
            self.ide,
            self.nombre,
            self.categoria,
            self.precio,
            self.stock,
            self.socketCpu,
            self.tipoRam,
        ]
