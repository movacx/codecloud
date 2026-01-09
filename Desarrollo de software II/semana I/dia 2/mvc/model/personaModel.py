class personaModel:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        
    def obtenerDatos(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Género: {self.genero}"