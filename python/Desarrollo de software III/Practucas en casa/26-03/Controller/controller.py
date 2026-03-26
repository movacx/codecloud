from Model.clienteModel import Cliente
from Model.libroModel import Libro
from Model.prestamoModel import PrestamoModel
from Model.Repositorio import Prestamo
class Controller:
    def __init__(self):
        self.repoLibro = Prestamo()
        self.repoCliente = Prestamo()
        self.repoPrestamo = Prestamo()
        