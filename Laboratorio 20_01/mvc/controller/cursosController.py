#Participantes: 
#Herlin Fabian Chavarria Beita C5E187
#Joseph Campos C4D660
#David Mora Gomez C5H441

from model.cursosModel import Curso
import view.cursosView as vistaCursos

class CursosController:
    def __init__(self):
        self.listaCursos = []
        
    #----------------------- MostrarDatos ------------------------------------
    def mostrarDatos(self):
        if not self.listaCursos:
            return vistaCursos.mostrarMensaje("No hay datos")
        else:
            for item in self.listaCursos:
                vistaCursos.mostrarTodos(item.mostrarDatos())
            
    #----------------------- AgregarCursos ------------------------------------
    def agregarCurso(self, nombreCurso, codigo, profesorAsignado):
        nuevoCurso = Curso(nombreCurso, codigo, profesorAsignado)
        self.listaCursos.append(nuevoCurso)
        return vistaCursos.mostrarMensaje("Agregado Correctamente")

    #----------------------- BuscarCursos ------------------------------------
    def buscarCursos(self, buscarCurso):
        encontrado = False
        for item in self.listaCursos:
            if item.getNombreCurso() == buscarCurso:
                vistaCursos.mostrarUno(item.mostrarDatos())
                encontrado = True
                break
        
        if not encontrado:
            vistaCursos.mostrarMensaje("No se encontro curso")
                
    #----------------------- EliminarCursos ------------------------------------
    def eliminarCursos(self, buscarCurso):
        for item in self.listaCursos:
            # Usamos getNombreCurso() porque la clase Curso no hereda de Persona
            if item.getNombreCurso() == buscarCurso:
                self.listaCursos.remove(item)
                return vistaCursos.mostrarMensaje("Eliminado Correctamente")
        
        return vistaCursos.mostrarMensaje("No se encontro curso")
                
    #----------------------- ModificarCursos -----------------------------------
    def modificarCursos(self, buscarCurso, nuevoDato, opcion):
        for item in self.listaCursos:
            if item.getNombreCurso() == buscarCurso:
                if opcion == 1:
                    item.setNombreCurso(nuevoDato)
                    return vistaCursos.mostrarMensaje("Nombre modificado con exito!")
                elif opcion == 2:
                    item.setCodigo(int(nuevoDato))
                    return vistaCursos.mostrarMensaje("Codigo modificado con exito!")
                elif opcion == 3:
                    item.setProfesorAsignado(nuevoDato)
                    return vistaCursos.mostrarMensaje("Profesor cambiado con exito!")
        
        return vistaCursos.mostrarMensaje("No se encontro Curso")