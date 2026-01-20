from model.estudianteModel import Estudiante
import view.estudianteView as vistaEstudiante

class EstudianteController:
    def __init__(self):
        self.lista = []
    
    #------------------Mostrar Datos----------------------------
    def mostrarDatos(self):
        for items in self.lista:
            print(items.mostrarDatos())
            
    #----------------------- AgregarObjeto ------------------------------------
    def agregarObjeto(self, nombre, apellidos, edad, telefono, direccion, fechaNacimiento, grado, correo):
        nuevoObjeto = Estudiante(nombre, apellidos, edad, telefono, direccion, fechaNacimiento, grado, correo)
        self.lista.append(nuevoObjeto)
        return vistaEstudiante.mostrarMensaje("Agregado Correctamente")
    
    #----------------------- buscarObjeto ------------------------------------
    def buscarObjeto(self, nombre):
        for items in self.lista:
            if items.getNombre() == nombre:
                vistaEstudiante.mostrarMensaje(f"{items.mostrarDatos()}")
                
    #----------------------- EliminarEstudiante ------------------------------------
    def eliminarEstudiante(self, nombre):
        EstudianteController.buscarObjeto(nombre)
        if EstudianteController.getNombre() == nombre:
            return "Encontrado"
        else:
            return "No encontrado"
