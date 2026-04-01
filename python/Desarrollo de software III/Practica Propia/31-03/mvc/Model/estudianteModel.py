class Estudiante:
    def __init__(self, id, carnet, nombre, apellido, carrera):
        self.id = id
        self.carnet = carnet
        self.nombre = nombre
        self.apellido = apellido
        self.carrera = carrera

    def __str__(self):
        return f'''
Carnet: {self.carnet}
Nombre: {self.nombre}
Apellido: {self.apellido}
Carrera: {self.carrera}'''
    

    def setId(self, nuevoId):
        self.id = nuevoId

    

    def exportar(self):
        return ([self.id, self.carnet, self.apellido, self.carrera])
