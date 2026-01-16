from Model.estudianteModel import Estudiante
import View.estudianteView as vistaEstudiante

class EstudianteController:
    def __init__(self):
        self.listaEstudiantes = []
        
    #----------------------- AgregarEstudiante ------------------------------------
    def mostrarDatos(self):
        for items in self.listaEstudiantes:
            vistaEstudiante.mostrarTodos(items.mostrarEstudiantes())
            
            
    #----------------------- AgregarEstudiante ------------------------------------
    def agregarEstudiante(self, nombre, edad, grado, correo):
        estudianteNuevo = Estudiante(nombre,edad,grado,correo)
        self.listaEstudiantes.append(estudianteNuevo)
        vistaEstudiante.mostrarMensaje("Agregado Correctamente")
    
    def buscarEstudiante(self, buscarNombre):
        for items in self.listaEstudiantes:
            if items.getNombre() == buscarNombre:
                vistaEstudiante.mostrarUno(items)
        return -1
        