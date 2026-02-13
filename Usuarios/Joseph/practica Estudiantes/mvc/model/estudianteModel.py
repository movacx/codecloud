class Estudiante:
    def __init__(self, id, carnet, nombre, apellido, correo):
        self.id=id
        self.carnet=carnet
        self.nombre=nombre
        self.apellido=apellido
        self.correo=correo
        
    def setId(self, id):
        self.id=id
    
    def getId(self):
        return self.id
    
    def ImportarToCsv():
        return ([self.id, self.carnet, self.nombre, self.apellido, self.correo])