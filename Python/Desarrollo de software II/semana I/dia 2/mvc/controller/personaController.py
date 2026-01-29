from model.personaModel import personaModel
import view.personaView as _personaView

class personaController:
    
    def crearPersona(self, nombre, edad, genero):

        modelo_creado = personaModel(nombre, edad, genero)
        return modelo_creado

    def mostrarDatos(self, modelo_persona):
        _personaView.mostrarDatos(modelo_persona)
        
        