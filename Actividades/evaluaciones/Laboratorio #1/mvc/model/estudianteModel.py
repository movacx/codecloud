from model.personaModel import Persona

class Estudiante(Persona):
    idEstudiante = 0 

    def __init__(self, nombre, apellidos, edad, telefono, direccion, fechaNacimiento, grado, correo):
        super().__init__(nombre, apellidos, telefono, direccion, fechaNacimiento, correo)
        
        self.edad = edad
        self.grado = grado
        
        Estudiante.idEstudiante += 1 
        self.id = Estudiante.idEstudiante
        
    # Getters Propios
    def getEdad(self):
        return self.edad
    def getGrado(self):
        return self.grado
    
    # Setters Propios
    def setEdad(self, edad):
        self.edad = edad
    def setGrado(self, grado):
        self.grado = grado
        
    def mostrarDatos(self):
        return f"[ID: {self.id}] {super().mostrarDatos()} | Edad: {self.edad} | Grado: {self.grado}"