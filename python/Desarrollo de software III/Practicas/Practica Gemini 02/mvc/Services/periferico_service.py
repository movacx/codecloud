
from Model.periferico import Periferico

class PerifericoService:
    def __init__(self, repository):
        self.repo = repository

    def agregar(self, modelo, tipo, precio):

        if not modelo.strip():
            raise ValueError('Debe de completar los campos.')
        if not tipo.strip():
            raise ValueError('El tipo es obligatorio')
        if precio <= 0:
            raise ValueError('Ingrese un monto valido')


        nuevo_periferico = Periferico(modelo, tipo, precio)
        self.repo.agregar(nuevo_periferico)

    def mostrar_datos(self):
        return self.repo.obtener_todos()