class UsuarioModel:
    def __init__(self, id, nombre, password, correo, rol):
        self.id = id
        self.nombre = nombre
        self.password = password
        self.correo = correo
        self.rol = rol

    def setNombre(self, nuevoNombre):
        self.nombre = nuevoNombre

    def setPassword(self, nuevaPassword):
        self.password = nuevaPassword

    def setCorreo(self, nuevoCorreo):
        self.correo = nuevoCorreo
        
    