#nombre, especialidad, telefono, correo
class Profesor:
    idProfesor = 0
    def __init__(self, nombre, especialidad, telefono, correo):
        self.nombre = nombre
        self.especialidad = especialidad
        self.telefono = telefono
        self.correo = correo
        Profesor.idProfesor =+1
        self.id = Profesor.idProfesor
        
    #Getters
    def getNombre(self):
        return self.nombre
    def getEspecialidad(self):
        return self.especialidad
    def getTelefono(self):
        return self.telefono
    def getCorreo(self):
        return self.correo
    
    #Setters
    def setNombre(self, nombre):
        self.nombre = nombre
    def setEspecialidad(self, especialidad):
        self.especialidad = especialidad
    def setTelefono(self, telefono):
        self.telefono = telefono
    def setCorreo(self, correo):
        self.correo = correo
        
    def __str__(self):
        return f"""
    Nombre: {self.nombre}
    Especialidad: {self.especialidad}
    Telefono: {self.telefono}
    Correo: {self.correo}"""
    
    def mostrarProfesores(self):
        return self.nombre, self.especialidad, self.telefono, self.correo
        