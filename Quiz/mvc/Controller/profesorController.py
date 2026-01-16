from Model.profesorModel import Profesor
import View.profesorView as vistaProfesor

class ProfesorController:
    def __init__(self):
        self.listaProfesores = []
        
        
    #----------------------- MostrarDatos ------------------------------------
    def mostrarDatos(self):
        if self.listaProfesores == None:
            return "No hay datos"
        else:
            for items in self.listaProfesores:
                vistaProfesor.mostrarTodos(items.mostrarProfesores())
        
            
    #----------------------- Agregar Profesor ------------------------------------
    def agregarProfesor(self, nombre, especialidad, telefono, correo):
        profesorNuevo = Profesor(nombre, especialidad, telefono, correo)
        self.listaProfesores.append(profesorNuevo)
        return vistaProfesor.mostrarMensaje("Agregado Correctamente")
    
    
    
    
    
    #----------------------- Buscar Profesor ------------------------------------
    def buscarProfesor(self, buscarNombre):
        for items in self.listaProfesores:
            if items.getNombre() == buscarNombre:
                vistaProfesor.mostrarUno(items)
                
                
    #----------------------- EliminarProfesor------------------------------------
    def eliminarProfesor(self, buscarNombre):
        for indice in self.listaProfesores:
            if indice.getNombre() == buscarNombre:
                self.listaProfesores.remove(indice)
                return vistaProfesor.mostrarMensaje("Eliminado Correctamente")
            else:
                return vistaProfesor.mostrarMensaje("No se encontro estudiante")
            
            
                 
    #----------------------- ModificarProfesor -----------------------------------
    def modificarProfesor(self, buscarProfesor, nuevoDato, opcion):
        for items in self.listaProfesores:
            if items.getNombre() == buscarProfesor:
                if opcion == 1:
                    items.setNombre(nuevoDato)
                    return vistaProfesor.mostrarMensaje("Nombre modificado con exito!")
                elif opcion == 2:
                    items.setEspecialidad(nuevoDato)
                    return vistaProfesor.mostrarMensaje("Edad modificado con exto!")
                elif opcion == 3:
                    items.setTelefono(nuevoDato)
                    return vistaProfesor.mostrarMensaje("Grado modificado con exto!")
                elif opcion == 4:
                    items.setCorreo(nuevoDato)
                    return vistaProfesor.mostrarMensaje("Correo modificado con exto!")
                else:
                    vistaProfesor.mostrarMensaje("No se encontro Profesor")
        
                    
