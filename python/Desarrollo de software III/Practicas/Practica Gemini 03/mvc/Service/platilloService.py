from Model.platilloModel import Platillo

class PlatilloService:
    def __init__(self, repo):
        self.repo = repo

    def registrar(self, nombre, precio, categoria):
        if not nombre.strip():
            raise ValueError('Debe de completar los campos.')
        if precio < 0:
            raise ValueError('El precio debe ser superior a 0')
        if not categoria.strip():
            raise ValueError('La categoria es obligatoria')

        nuevo_platillo = Platillo(nombre,precio,categoria)
        self.repo.agregar(nuevo_platillo)

    def imprimir_dato(self):
        return self.repo.cargar_todos()

    def buscar_por_nombre(self, nombre):
        if not nombre.strip():
            raise ValueError('El nombre es obligatorio')

        return self.repo.buscar_por(nombre)
