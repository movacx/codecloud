from model.personaModel import personaModel
import view.personaView as _personaView

class personaController:
    def crearPersona(self, nombre, edad, genero):
        _personaView = personaModel()