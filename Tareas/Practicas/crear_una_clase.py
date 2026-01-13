

def validarExistencia(nombre):
    if nombre in lista:
        return True
    else:
        return False

def buscar(nombre):
    if validarExistencia(nombre) == True:
        indice = lista.index(nombre)
    else:
        return f"No se encontro {nombre} en la lista"

    
def modificar(indice,nombreModificar):
   lista[indice] = nombreModificar
   


def eliminar(nombre):
    print("eliminar")


def mostrar():
    print("La lista contiene: ", lista)


lista = ["Fabian","Lucas","Samuel","Fiorella"]


print(modificar(1,"Pene"))

numeros = [1,2,3,4,5,6]
numeros[0] = 10
print(numeros)



