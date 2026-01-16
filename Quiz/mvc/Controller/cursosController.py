from Model.cursosModel import Curso
import View.cursosView as vistaCursos

class CursosController:
    def init(self):
        self.listaCursos = []


    #----------------------- AgregarCursos ------------------------------------
    def mostrarDatos(self):
        for items in self.listaCursos:
            vistaCursos.mostrarTodos(items.mostrarCursos())


    #----------------------- AgregarCursos ------------------------------------
    def agregarCursos(self, nombreCurso,codigo, profesorAsignado):
        CursosNuevo = Curso(nombreCurso,codigo, profesorAsignado)
        self.listaCursos.append(CursosNuevo)
        return vistaCursos.mostrarMensaje("Agregado Correctamente")

    def buscarCursos(self, buscarNombre):
        for items in self.listaCursos:
            if items.getNombreCurso() == buscarNombre:
                vistaCursos.mostrarUno(items)

    #----------------------- EliminarCursos ------------------------------------
    def eliminarCursos(self, buscarNombre):
        for indice in self.listaCursos:
            if indice.getNombreCurso() == buscarNombre:
                self.listaCursos.remove(indice)
                return vistaCursos.mostrarMensaje("Eliminado Correctamente")
            else:
                return vistaCursos.mostrarMensaje("No se encontro Cursos")

    #----------------------- ModificarCursos -----------------------------------
    def modificarCursos(self, buscarCursos, nuevoCurso, opcion):
        for items in self.listaCursos:
            if items.getNombreCurso() == buscarCursos:
                if opcion == 1:
                    items.setNombreCurso(nuevoCurso)
                    return
vistaCursos.mostrarMensaje("No se encontro Cursos")