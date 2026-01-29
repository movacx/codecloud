#Mi variables
personas = ["Mario", "Isaac", "Alberto","Sasha"]
textoRespuesta = ""

#Funciones
def buscar(usuarioNombre):
    if usuarioNombre in personas:
        indice =personas.index(usuarioNombre)
    else:
        indice =-1
    return indice
    

def modificar(nombre):
    print("Modificando")

def borrar(nombre):
    if nombre in personas:
     personas.remove(nombre)
    else:
        return "No se encontro "
    

print("Los usuarios del sistema: ", personas)
#modificar()
usuarioNuevo = input("Ingrese un nuevo usuario: ")
personas.append(usuarioNuevo)#Insertar elementos en un arreglo

print("Los usuarios del sistema", personas)

usuarioNombre = input("Ingrese el usuario a buscar: ")
posicion = buscar(usuarioNombre)



if posicion == -1:
    textoRespuesta = "No encontro datos para"
else:
    textoRespuesta = "Se encontro datos para"    

print (textoRespuesta, usuarioNombre, "en el identificador: ", posicion)

#La seccion de buscar
#La seccion de modificar
#La seccion de borrar
#= es para asignar un valor
#== es para comparar un valor
#=== es para comparar un valor + el tipo de dato