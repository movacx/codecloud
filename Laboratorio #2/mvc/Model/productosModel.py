class Productos:
	
	idProducto = 0
	def __init__(self, codigoUnico,nombre, Categoria,precio,stock,cantidad, tipoMoviento, fecha):
		self.codigoUnico = codigoUnico
		self.nombre = nombre
		self.categoria = categoria
		self.precio = precio
		self.stock = stock
		self.cantidad = cantidad
		self.tipoMoviento = tipoMoviento
		self.fecha = fecha
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
	
	def getCantidad(self):
		return self.cantidad
	
	def getTipoMoviento(self):
		return self.tipoMoviento
	
	def getFecha(self):
		self.fecha
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
		
	def setCantidad(self, cantidad):
		self.cantidad = cantidad
	
	def setTipoMoviento(self, tipoMoviento):
		self.tipoMoviento = tipoMoviento
		
	def setPrecio(self, precio):
		self.precio = precio
		
	
	def mostrarDatos(self):
		return f" Codigo : {self.codigoUnico} Nombre: {self.nombre} Categoria: {self.categoria} Precio: {self.precio} Stock: {self.stock} Cantidad: {self.cantidad} TipoMoviento: {self.tipoMoviento} Fecha: {self.fecha}"
