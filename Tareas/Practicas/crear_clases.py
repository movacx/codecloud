class inventario:
    
    idMovil = 1
    def __init__(self, marca, almacenamiento, ram):
        self.marca = marca
        self.almacenamiento = almacenamiento
        self.ram = ram
        self.idMovil = inventario.idMovil
        inventario.idMovil +=1

    
    def mostrarDato(self):
        return f"Marca: {self.marca}", f"Almacenamiento: {self.almacenamiento}", f"Ram: {self.ram},", f"IdMovil: {self.idMovil}"

    
    
    #Seccion de gets
    def getMarca(self):
        return self.marca
    
    def getAlmacenamiento(self):
        return self.almacenamiento
    
    def getRam(self):
        return self.ram
    
    def getidMovil(self):
        return self.idMovil
    
    
lista_inventario = []


##agregar
def agregarInventario(marca, almacenamiento, ram):
    lista_inventario.append(inventario(marca,almacenamiento,ram))
    return "Agregado con exito!" 

##buscar por marca
def buscar(marca):
    for items in lista_inventario:
        if marca == items.getMarca():
            indice = lista_inventario.index(items)
            return f"Encontrado en la posicion: {[indice]}, y contiene: {items}"
        
    return "No encontrado"


##modificar
def modificar(nombre, edad):
    return True
    

##eliminar
def eliminar(marca):
    for items in lista_inventario:
        if marca == items.getMarca():
            indice = lista_inventario.index(marca)
            lista_inventario.remove(indice)
            return "eliminado con exito!"
    return "No se pudo eliminar"
    
##mostrar
def mostrar():
   print("Los telefonos ingresados en el sistema: ", lista_inventario)
   for items in lista_inventario:
        print(items.mostrarDato())
        resultadoTemporal = "El nombre es:", items.getMarca()

    
agregarInventario("Google Pixel", 128, 16)
agregarInventario("Iphone", 250, 32)
print(buscar("Google Pixel"))

print(mostrar())



        