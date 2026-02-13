from Model.fileUsuarioModel import UsuarioModel

class AdminModel(UsuarioModel):

    def __init__(self, id, nombre, password, correo):
        super().__init__(id, nombre, password, correo, rol='Administrador')
        
    def importar(self):
        return ([self.id, self.nombre, self.password, self.correo, self.rol])