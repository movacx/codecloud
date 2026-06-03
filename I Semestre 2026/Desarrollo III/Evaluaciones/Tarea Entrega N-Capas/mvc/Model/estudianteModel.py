class Estudiante:
    def __init__(self, carnet, nombre, carrera):
        self.carnet = carnet
        self.nombre = nombre
        self.carrera = carrera

    def to_dict(self):
        return {
            'Carnet':self.carnet,
            'Nombre':self.nombre,
            'Carrera':self.carrera
        }

    def __str__(self):
        return self.carnet, self.nombre, self.carrera