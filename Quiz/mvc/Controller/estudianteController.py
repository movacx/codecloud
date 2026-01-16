
from Model.estudianteModel import Estudiante
import View.estudianteView as vista


listaEstudiante = []
#----------------------- Agregar Estudiante ----------------------------------
def agregarEstudiante(nombre, edad, grado, correo):
    nuevoEstudiante = Estudiante(nombre, edad, grado, correo)
    listaEstudiante.append(nuevoEstudiante)
    return 1

#----------------------- Buscar Estudiante -----------------------------------
def buscarEstudiante(nombreBuscar):
    for items in listaEstudiante:
        if items.getNombre() == nombreBuscar:
            return items
    return -1
            
#---------------------- Eliminar Estudiante ----------------------------------
def eliminarEstudiante(nombreBorrar):
    for items in listaEstudiante:
        if items.getNombre() == nombreBorrar:
            listaEstudiante.remove(items)
            return 1
    return -1

#---------------------- Modificar Estudiante --------------------------------
def modificarEstudiante(nombreBuscar, nuevoDato):
    usuarioEncontrado = buscarEstudiante(nombreBuscar)
    if usuarioEncontrado:
        usuarioEncontrado.setNombre(nuevoDato)
        return "Nombre modificado"
    return "No encontrado"

def mostrarDatos(buscarDatos):
    for items in listaEstudiante:
        if items.getNombre() == buscarDatos:
            return items.mostrarEstudiantes()
    return -1
    
