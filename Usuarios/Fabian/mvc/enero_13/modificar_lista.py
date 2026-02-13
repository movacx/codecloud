def validarExistencia(nombre):
    if nombre in lista:
        return True
    else:
        return False

def agregar(nombre):
    lista.append(nombre)
    return f"{nombre}, agregado con exito!"
    
def buscar(nombre): #Funcional
    if validarExistencia(nombre) == True:
        indice = lista.index(nombre)
    else:
        return f"No se encontro {nombre} en la lista"
    return f"{nombre}, se encuentra en la posicion: {indice}"

def eliminar(nombre):
    if validarExistencia(nombre) == True:
        lista.remove(nombre)
        return f"{nombre}, eliminado con exito!"
    else:
        return False

def modificar_buscar(nombre, indice):
    lista[indice] = nombre
    return f"Modificar con exito! Nuevo nombre: {nombre}, en la posicion [{indice}]"


def mostrar(): #Funcional
    print("La lista contiene: ", lista)


lista = ["Fabian","Lucas","Samuel","Fiorella"]

print(buscar("Fabian"))
print(agregar("Mariano"))
print(eliminar("Lucas"))
print(modificar_buscar("Cristian", 2))


mostrar()

