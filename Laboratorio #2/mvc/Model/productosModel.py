class Productos:
	
	idProducto = 0
	def __init__(self, codigoUnico,nombre, Categoria,precio,stock):
		self.codigoUnico = codigoUnico
		self.nombre = nombre
		self.categoria = categoria
		self.precio = precio
		self.stock = stock
		Productos.idProducto += 1
		self.id = Productos.idProducto
	
	#Getters
	def getCodigoUnico(self):
		return self.codigoUnico
	
	def getNombre(self):
		return self.nombre
	
	def getCategoria(self):
		return self.categoria
	
	def getPrecio(self):
		return self.precio
	
	def getStock(self):
		self.stock
	
	#Setters
	def setCodigoUnico(self, codigoUnico):
		self.codigoUnico = codigoUnico
	
	def setNombre(self, nombre):
		self.nombre = nombre
	
	def setCategoria(self, categoria):
		self.categoria = categoria
	
	def setPrecio(self, precio):
		self.precio = precio
	
	def setStock(self, stock):
		self.stock = stock
		
	
	def mostrarDatos(self):
		return f" Codigo : {self.codigoUnico} Nombre: {self.nombre} Categoria: {self.categoria} Precio: {self.precio} Stock: {self.stock}"
