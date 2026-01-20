class Persona:
    contador = 0
    def __init__(self, nombre, apellidos, telefono, direccion, fechaNacimiento, correo):
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.direccion = direccion
        self.fechaNacimiento = fechaNacimiento
        self.correo = correo
        



    # Getters
    def getNombre(self):
        return self.nombre
    def getApellidos(self):
        return self.apellidos
    def getTelefono(self):
        return self.telefono
    def getDireccion(self):
        return self.direccion
    def getFechaNacimiento(self):
        return self.fechaNacimiento
    def getCorreo(self):
        return self.correo

    # Setters
    def setNombre(self, nombre):
        self.nombre = nombre
    def setApellidos(self, apellidos):
        self.apellidos = apellidos
    def setTelefono(self, telefono):
        self.telefono = telefono
    def setDireccion(self, direccion):
        self.direccion = direccion
    def setFechaNacimiento(self, fechaNacimiento):
        self.fechaNacimiento = fechaNacimiento
    def setCorreo(self, correo):
        self.correo = correo


    def mostrarDatos(self):
        return f"Nombre: {self.nombre} {self.apellidos} | Tel: {self.telefono} | Correo: {self.correo} | Dir: {self.direccion}"