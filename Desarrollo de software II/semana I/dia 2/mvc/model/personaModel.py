class personaModel:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        
    def obtenerDatos(self):
        # Retorna el string para que la vista lo imprima
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Género: {self.genero}"