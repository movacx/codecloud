#Participantes: 
#Herlin Fabian Chavarria Beita C5E187
#Joseph Campos C4D660
#David Mora Gomez C5H441

from model.estudianteModel import Estudiante
import view.estudianteView as vistaEstudiante

class EstudianteController:
    def __init__(self):
        self.listaEstudiantes = []
        
    #----------------------- MostrarDatos ------------------------------------
    def mostrarDatos(self):
        if not self.listaEstudiantes:
            return vistaEstudiante.mostrarMensaje("No hay datos")
        else:
            for item in self.listaEstudiantes:
                vistaEstudiante.mostrarTodos(item.mostrarDatos())
        
    #----------------------- AgregarEstudiante ------------------------------------
    def agregarEstudiante(self, nombre, apellidos, edad, telefono, direccion, fechaNacimiento, grado, correo):
        estudianteNuevo = Estudiante(nombre, apellidos, edad, telefono, direccion, fechaNacimiento, grado, correo)
        self.listaEstudiantes.append(estudianteNuevo)
        return vistaEstudiante.mostrarMensaje("Agregado Correctamente")
    
    #----------------------- BuscarEstudiante ------------------------------------
    def buscarEstudiante(self, buscarNombre):
        encontrado = False
        for item in self.listaEstudiantes:
            if item.getNombre() == buscarNombre:
                vistaEstudiante.mostrarUno(item.mostrarDatos())
                encontrado = True
                break
        if not encontrado:
            vistaEstudiante.mostrarMensaje("No se encontró estudiante con ese nombre")
                
    #----------------------- EliminarEstudiante ------------------------------------
    def eliminarEstudiante(self, buscarNombre):
        for item in self.listaEstudiantes:
            if item.getNombre() == buscarNombre:
                self.listaEstudiantes.remove(item)
                return vistaEstudiante.mostrarMensaje("Eliminado Correctamente")
        return vistaEstudiante.mostrarMensaje("No se encontro estudiante")
                
    #----------------------- ModificarEstudiante -----------------------------------
    def modificarEstudiante(self, buscarEstudiante, nuevoDato, opcion):
        for item in self.listaEstudiantes:
            if item.getNombre() == buscarEstudiante:
                if opcion == 1:
                    item.setNombre(nuevoDato)
                    return vistaEstudiante.mostrarMensaje("Nombre modificado con exito!")
                elif opcion == 2:
                    item.setEdad(int(nuevoDato))
                    return vistaEstudiante.mostrarMensaje("Edad modificada con exito!")
                elif opcion == 3:
                    item.setGrado(nuevoDato)
                    return vistaEstudiante.mostrarMensaje("Grado modificado con exito!")
                elif opcion == 4:
                    item.setCorreo(nuevoDato)
                    return vistaEstudiante.mostrarMensaje("Correo modificado con exito!")
                
        return vistaEstudiante.mostrarMensaje("No se encontro Estudiante para modificar")