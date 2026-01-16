from Model.cursosModel import Curso
import View.cursosView as vistaCursos

class CursosController:
    def __init__(self):
        self.listaCursos = []
        
        
    #----------------------- MostrarDatos ------------------------------------
    def mostrarDatos(self):
        if self.listaCursos == None:
            return "No hay datos"
        else:
            for items in self.listaCursos:
                vistaCursos.mostrarTodos(items.mostrarCursos())
        
            
    #----------------------- AgregarEstudiante ------------------------------------
    def agregarEstudiante(self, nombreCurso,codigo, profesorAsignado):
        nuevoCurso = Curso(nombreCurso,codigo, profesorAsignado)
        self.listaCursos.append(nuevoCurso)
        return vistaCursos.mostrarMensaje("Agregado Correctamente")
    
    
    
    
    
    
    
    def buscarEstudiante(self, buscarCurso):
        for items in self.listaCursos:
            if items.getNombreCurso() == buscarCurso:
                vistaCursos.mostrarUno(items)
                
                
                
                
                
                
                
                
                
                
                
                
    #----------------------- EliminarEstudiante ------------------------------------
    def eliminarEstudiante(self, buscarCurso):
        for indice in self.listaCursos:
            if indice.getNombreCurso() == buscarCurso:
                self.listaCursos.remove(indice)
                return vistaCursos.mostrarMensaje("Eliminado Correctamente")
            else:
                return vistaCursos.mostrarMensaje("No se encontro estudiante")
                
                
                
                
                
                
                
                
                
                
    def setNombreCurso(self,nombreCurso):
        self.nombreCurso = nombreCurso
    
    def setCodigo(self,codigo):
        self.codigo = codigo
    
    def setProfesorAsignado(self,profesorAsignado):
        self.profesorAsignado = profesorAsignado 
                
                
                
                
    #----------------------- ModificarEstudiante -----------------------------------
    def modificarEstudiante(self, buscarCurso, nuevoDato, opcion):
        for items in self.listaCursos:
            if items.getNombreCurso() == buscarCurso:
                if opcion == 1:
                    items.setNombreCurso(nuevoDato)
                    return vistaCursos.mostrarMensaje("Nombre modificado con exito!")
                elif opcion == 2:
                    items.setCodigo(nuevoDato)
                    return vistaCursos.mostrarMensaje("Edad modificado con exto!")
                elif opcion == 3:
                    items.setProfesorAsignado(nuevoDato)
                    return vistaCursos.mostrarMensaje("Grado modificado con exto!")
            return vistaCursos.mostrarMensaje("No se encontro Estudiante")
                    
