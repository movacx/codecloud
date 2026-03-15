#Participantes: 
#Herlin Fabian Chavarria Beita C5E187
#Joseph Campos C4D660
#David Mora Gomez C5H441

from model.profesorModel import Profesor
import view.profesorView as vistaProfesor

class ProfesorController:
    def __init__(self):
        self.listaProfesores = []
        
    #----------------------- MostrarDatos ------------------------------------
    def mostrarDatos(self):
        if not self.listaProfesores:
            return vistaProfesor.mostrarMensaje("No hay datos")
        else:
            for item in self.listaProfesores:
                vistaProfesor.mostrarTodos(item.mostrarDatos())
            
    #----------------------- Agregar Profesor ------------------------------------
    def agregarProfesor(self, nombre, apellidos, especialidad, telefono, direccion, fechaNacimiento, correo):
        profesorNuevo = Profesor(nombre, apellidos, especialidad, telefono, direccion, fechaNacimiento, correo)
        self.listaProfesores.append(profesorNuevo)
        return vistaProfesor.mostrarMensaje("Agregado Correctamente")
    
    #----------------------- Buscar Profesor ------------------------------------
    def buscarProfesor(self, buscarNombre):
        encontrado = False
        for item in self.listaProfesores:
            if item.getNombre() == buscarNombre:
                vistaProfesor.mostrarUno(item.mostrarDatos())
                encontrado = True
                break
        
        if not encontrado:
            vistaProfesor.mostrarMensaje("No se encontró profesor")
                
    #----------------------- EliminarProfesor------------------------------------
    def eliminarProfesor(self, buscarNombre):
        for item in self.listaProfesores:
            if item.getNombre() == buscarNombre:
                self.listaProfesores.remove(item)
                return vistaProfesor.mostrarMensaje("Eliminado Correctamente")
        return vistaProfesor.mostrarMensaje("No se encontro profesor")
            
    #----------------------- ModificarProfesor -----------------------------------
    def modificarProfesor(self, buscarProfesor, nuevoDato, opcion):
        for item in self.listaProfesores:
            if item.getNombre() == buscarProfesor:
                if opcion == 1:
                    item.setNombre(nuevoDato)
                    return vistaProfesor.mostrarMensaje("Nombre modificado con exito!")
                elif opcion == 2:
                    item.setEspecialidad(nuevoDato)
                    return vistaProfesor.mostrarMensaje("Especialidad modificada con exito!")
                elif opcion == 3:
                    item.setTelefono(int(nuevoDato))
                    return vistaProfesor.mostrarMensaje("Telefono modificado con exito!")
                elif opcion == 4:
                    item.setCorreo(nuevoDato)
                    return vistaProfesor.mostrarMensaje("Correo modificado con exito!")
                
        return vistaProfesor.mostrarMensaje("No se encontro Profesor")