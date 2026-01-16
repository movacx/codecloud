#nombre, edad, grado, correo
class Estudiante:
    idEstudiante = 0
    def __init__(self, nombre, edad, grado, correo):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        self.correo = correo
        Estudiante.idEstudiante =+1
        self.id = Estudiante.idEstudiante
        
    #Getters
    def getNombre(self):
        return self.nombre
    def getEdad(self):
        return self.edad
    def getGrado(self):
        return self.grado
    def getCorreo(self):
        return self.correo
    
    #Setters
    def setNombre(self, nombre):
        self.nombre = nombre
    def setEdad(self, edad):
        self.edad = edad
    def setGrado(self, grado):
        self.grado = grado
    def setCorreo(self, correo):
        self.correo = correo
        
    def __str__(self):
        return f"""
    """
        
    
    