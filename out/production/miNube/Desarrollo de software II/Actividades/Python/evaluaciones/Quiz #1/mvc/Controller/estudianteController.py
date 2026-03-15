#Participantes: 
#Herlin Fabian Chavarria Beita C5E187
#Joseph Campos C4D660
#David Mora Gomez C5H441

from Model.estudianteModel import Estudiante
import View.estudianteView as vistaEstudiante

class EstudianteController:
    def __init__(self):
        self.listaEstudiantes = []
        
        
    #----------------------- MostrarDatos ------------------------------------
    def mostrarDatos(self):
        if self.listaEstudiantes == None:
            return "No hay datos"
        else:
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
                
            else:
                return vistaEstudiante.mostrarMensaje("No se encontro estudiante")
                
    #----------------------- ModificarEstudiante -----------------------------------
    def modificarEstudiante(self, buscarEstudiante, nuevoDato, opcion):
        for items in self.listaEstudiantes:
            if items.getNombre() == buscarEstudiante:
                if opcion == 1:
                    items.setNombre(nuevoDato)
                    return vistaEstudiante.mostrarMensaje("Nombre modificado con exito!")
                elif opcion == 2:
                    items.setEdad(nuevoDato)
                    return vistaEstudiante.mostrarMensaje("Edad modificado con exto!")
                elif opcion == 3:
                    items.setGrado(nuevoDato)
                    return vistaEstudiante.mostrarMensaje("Grado modificado con exto!")
                elif opcion == 4:
                    items.setCorreo(nuevoDato)
                    return vistaEstudiante.mostrarMensaje("Correo modificado con exto!")
            return vistaEstudiante.mostrarMensaje("No se encontro Estudiante")
                    
