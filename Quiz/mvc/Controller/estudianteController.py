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
        return vistaEstudiante.mostrarMensaje("Agregado Correctamente")
    
    def buscarEstudiante(self, buscarNombre):
        for items in self.listaEstudiantes:
            if items.getNombre() == buscarNombre:
                vistaEstudiante.mostrarUno(items)
                
    #----------------------- EliminarEstudiante ------------------------------------
    def eliminarEstudiante(self, buscarNombre):
        for indice in self.listaEstudiantes:
            if indice.getNombre() == buscarNombre:
                self.listaEstudiantes.remove(indice)
                return vistaEstudiante.mostrarMensaje("Eliminado Correctamente")
            else:
                return vistaEstudiante.mostrarMensaje("No se encontro estudiante")
                
        