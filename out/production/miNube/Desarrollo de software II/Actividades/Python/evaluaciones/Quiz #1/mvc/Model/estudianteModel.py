
#Participantes: 
#Herlin Fabian Chavarria Beita C5E187
#Joseph Campos C4D660
#David Mora Gomez C5H441

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
    def getIdEstudiante(self):
        return self.id
    
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
    Nombre: {self.nombre}
    Edad: {self.edad}
    Grado: {self.grado}
    Correo: {self.correo}"""
    
    def mostrarEstudiantes(self):
        return self.nombre, self.edad, self.grado, self.correo
        
    
    