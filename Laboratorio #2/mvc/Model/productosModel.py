class Producto:

    idProducto = 0 

    def __init__(self, nombre, categoria, precio, stock):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock
        Producto.idProducto += 1
        self.id = Producto.idProducto
        
#Getters
def getNombre(self):
    return self.nombre

def getCategoria(self):
    return self.categoria

def getPrecio(self):
    return self.precio

def getStock(self):
    return self.stock

#Setters
def setNombre(self, nombre):
    self.nombre = nombre

def setCategoria(self, categoria):
    self.categoria = categoria

def setPrecio(self, precio):
    self.precio = precio
    
def setStock(self, stock):
    self.stock = stock