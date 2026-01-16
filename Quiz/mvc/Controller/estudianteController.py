
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
def modificarEstudiante(nombreBuscar, nuevoDato, opcion):
    usuarioEncontrado = buscarEstudiante(nombreBuscar)
    if usuarioEncontrado:
        if opcion == 1:
            usuarioEncontrado.setNombre(nuevoDato)
            return "Nombre modificado"
        elif opcion == 2:
            usuarioEncontrado.setEdad(nuevoDato)
            return "Edad modificado!"
        elif opcion == 3:
            usuarioEncontrado.setGrado(nuevoDato)
            return "Grado modificado!"
        elif opcion == 4:
            usuarioEncontrado.setCorreo(nuevoDato)
            return "Correo modificado!"
        
    return "No encontrado"

#----------------------- Mostrar Todos los datos -----------------------------
def mostrarDatos():
    for items in listaEstudiante:
           print(items.mostrarEstudiantes())
    return -1
    
