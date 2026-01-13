class inventario:
    def __init__(self, marca, almacenamiento, ram):
        self.marca = marca
        self.almacenamiento = almacenamiento
        self.ram = ram

        
lista_inventario = []

##validar
def validarExistencias(marca):
    if marca in lista_inventario:
        return True
    else:
        return False

##agregar
def agregarInventario(marca, almacenamiento, ram):
    lista_inventario.append(inventario(marca,almacenamiento,ram))
    return "Agregado con exito!" 

##buscar por indice
def buscarpor_indice(indice):
    if validarExistencias == True:
        return
    else:
        return False

##modificar

##eliminar
def eliminar(indice):
    lista_inventario.pop(indice)
    
##mostrar
def mostrar():
    return lista_inventario
    
print(agregarInventario("Google Pixel", 128, 16))
print(mostrar())
print(eliminar(0))

        