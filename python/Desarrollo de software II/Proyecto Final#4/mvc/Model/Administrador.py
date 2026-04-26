from Usuario import Usuario


class Administrador(Usuario):
    def __init__(self, ide, correo, password, nombre, rol):
        super().__init__(ide, correo, password, nombre, rol)

    def importarToCsv(self):
        # El admin usa 'N/A' en direccion para mantener las columnas del CSV
        return [self.ide, self.correo, self.password, self.nombre, self.rol, "N/A"]
