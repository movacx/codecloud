from Usuario import Usuario
class Cliente(Usuario):
    def __init__(self, ide, correo, password, nombre, rol, direccion):
        super().__init__(ide, correo, password, nombre, rol)
        self.direccion = direccion

    def importarToCsv(self):
        return [self.ide, self.correo, self.password, self.nombre, self.rol, self.direccion]
