from Model.estudianteModel import Estudiante
from Model.libroModel import Libro
from Model.prestamoModel import Prestamo
from Model.repositorio import Repositorio

class Controller:
    def __init__(self):
        self.repo_estudiante = Repositorio()
        self.repo_libro = Repositorio()
        self.repo_prestamo = Repositorio()

    def registrar_estudiante(self, carnet, nombre, carrera):


