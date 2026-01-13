class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
    
    # Getters y Setters
    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, nombre):
        self._nombre = nombre
        
    def get_edad(self):
        return self._edad
        
    def set_edad(self, edad):
        self._edad = edad

    def __repr__(self): 
        return f"{self._nombre}"

personas = [] 

personas.append(Persona("Mario", 20))
personas.append(Persona("Isaac", 22))
personas.append(Persona("Alberto", 25))
personas.append(Persona("Sasha", 30))

textoRespuesta = ""

def mostrar():
    print("Los usuarios del sistema: ", personas)

def buscar(usuarioNombre):
    indice_encontrado = -1
    contador = 0
    
    for obj_persona in personas:
        if obj_persona.get_nombre() == usuarioNombre:
            indice_encontrado = contador
            break 
        contador = contador + 1
    return indice_encontrado

def modificar(nuevoNombre, indice):
    personas[indice].set_nombre(nuevoNombre)

def borrarAlumno(nombre):
    posicion = buscar(nombre)
    if posicion != -1:
        # pop elimina el objeto en esa posicion
        personas.pop(posicion) 
        print("El nombre:", nombre, "fue Eliminado")

mostrar()
usuarioNombreModificar = input("Ingrese el usuario a buscar y modificar: ")

posicion = buscar(usuarioNombreModificar)

if posicion == -1:
    textoRespuesta = "No encontro datos para", usuarioNombreModificar
else:
    nuevoNombre = input("Ingrese el nuevo nombre: ")
   
    modificar(nuevoNombre, posicion)
    textoRespuesta = "Se encontro datos para", usuarioNombreModificar    
print(textoRespuesta)
mostrar()