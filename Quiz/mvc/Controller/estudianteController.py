from Model.estudianteModel import Estudiante
import View.estudianteView as vistaEstudiante

class EstudianteController:
    def __init__(self):
        self.listaEstudiantes = []
        
    #----------------------- AgregarEstudiante ------------------------------------
    def agregarEstudiante(self, nombre, edad, grado, correo):
        estudianteNuevo = Estudiante(nombre,edad,grado,correo)
        self.listaEstudiantes.append(estudianteNuevo)
        vistaEstudiante.mostrarMensaje("Agregado Correctamente")
    
    