class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
   
        
lista_personas = []

#Funciones
def mostrar():
   print("Los usuarios del sistema: ", lista_personas)

def buscar(usuarioNombre):
    if usuarioNombre in lista_personas:
        indice = lista_personas.index(usuarioNombre)
    else:
        indice =-1
    return indice

def borrar(nombre):
    lista_personas.remove(nombre)
    print("El nombre: ",nombre," fue Eliminado")

def modificar(nombreModificar, indice):
   lista_personas[indice] = nombreModificar


def insertar(nombre, edad):
    nuevosDatos = persona(nombre, edad)
    lista_personas.append(nuevosDatos)
    print("Datos almacenados exitosamente")
    
#######################################################

nombre = input("Ingrese el nombre de la persona: ")
edad = input("Ingrese la edad de las personas: ")

insertar(nombre, edad)
mostrar()
