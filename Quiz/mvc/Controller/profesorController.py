from Model.profesorModel import Profesor
import View.profesorView as vistaProfesor

class ProfesorController:
    def __init__(self):
        self.listaProfesor = []
        
    #----------------------- AgregarEstudiante ------------------------------------
    def mostrarDatos(self):
        for items in self.listaProfesor:
            vistaProfesor.mostrarTodos(items.mostrarProfesor())
            
            
    #----------------------- AgregarEstudiante ------------------------------------
    def agregarProfesor(self, nombre, especialidad, telefono, correo):
        profesorNuevo = Profesor(nombre, especialidad, telefono, correo)
        self.listaProfesor.append(profesorNuevo)
        return vistaProfesor.mostrarMensaje("Agregado Correctamente")
    
    def buscarProfesor(self, buscarNombre):
        for items in self.listaProfesor:
            if items.getNombre() == buscarNombre:
                vistaProfesor.mostrarUno(items)
                
    #----------------------- EliminarEstudiante ------------------------------------
    def EliminarProfesor(self, buscarNombre):
        for indice in self.listaProfesor:
            if indice.getNombre() == buscarNombre:
                self.listaProfesor.remove(indice)
                return vistaProfesor.mostrarMensaje("Eliminado Correctamente")
            else:
                return vistaProfesor.mostrarMensaje("No se encontro estudiante")
                
    #----------------------- ModificarEstudiante -----------------------------------
    def modificarProfesor(self, buscarProfesor, nuevoDato, opcion):
        for items in self.listaProfesor:
            if items.getNombre() == buscarProfesor:
                if opcion == 1:
                    items.setNombre(nuevoDato)
                    return vistaProfesor.mostrarMensaje("Nombre modificado con exito!")
                elif opcion == 2:
                        items.setEdad(nuevoDato)
                        return vistaProfesor.mostrarMensaje("Edad modificado con exto!")
                elif opcion == 3:
                        items.setGrado(nuevoDato)
                        return vistaProfesor.mostrarMensaje("Grado modificado con exto!")
                elif opcion == 4:
                        items.setCorreo(nuevoDato)
                        return vistaProfesor.mostrarMensaje("Correo modificado con exto!")
            return vistaProfesor.mostrarMensaje("No se encontro Estudiante")