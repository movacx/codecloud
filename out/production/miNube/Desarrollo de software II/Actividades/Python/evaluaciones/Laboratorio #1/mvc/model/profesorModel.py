from model.personaModel import Persona

class Profesor(Persona):
    idProfesor = 0

    def __init__(self, nombre, apellidos, especialidad, telefono, direccion, fechaNacimiento, correo):
        super().__init__(nombre, apellidos, telefono, direccion, fechaNacimiento, correo)
        
        self.especialidad = especialidad
        
        Profesor.idProfesor += 1
        self.id = Profesor.idProfesor
        
    # Getters 
    def getEspecialidad(self):
        return self.especialidad
    
    # Setters
    def setEspecialidad(self, especialidad):
        self.especialidad = especialidad
    
    def mostrarDatos(self):
        return f"[ID: {self.id}] {super().mostrarDatos()} | Especialidad: {self.especialidad}"