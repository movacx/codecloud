
class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

personas = []
textoRespuesta = ""

#Funciones
def mostrar():
   print("Los usuarios del sistema: ", personas)
   

def buscar(usuarioNombre):
    if usuarioNombre in personas:
        indice = personas.index(usuarioNombre)
    else:
        indice =-1
    return indice

def borrar(nombre):
    #un if para verificar y eliminar
    #para evitar duplicar codigo
    # if usuarioNombre in personas:
    #     indice =personas.index(usuarioNombre)
    # else:
    #     indice =-1
    personas.remove(nombre)
    print("El nombre: ",nombre," fue Eliminado")

def modificar(nombreModificar, indice):
   personas[indice] = nombreModificar

def insertar(nombre, edad):
    nuevosDatos = persona(nombre, edad)
    personas.append(nuevosDatos)
    print("Datos almacenados existosamente")


###################################Aca va el sistema

nombre = input("Ingrese el nombre de la persona: ")
edad = input("Ingrese la edad de la persona: ")

insertar(nombre, edad)
mostrar()
#La seccion de buscar
#La seccion de modificar
#La seccion de borrar
#= es para asignar un valor
#== es para comparar un valor
#=== es para comparar un valor + el tipo de dato