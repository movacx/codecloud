from Model.fileUsuarioModel import UsuarioModel
class Cliente(UsuarioModel):
    
    def __init__(self, id, nombre, password, correo, direccion, tarjeta):
        super().__init__(id, nombre, password, correo, rol="Cliente")
        self.direccion = direccion
        self.tarjeta = tarjeta

    def importar(self):
        return ([self.id, self.nombre, self.password, self.correo, self.direccion, self.tarjeta, self.rol])