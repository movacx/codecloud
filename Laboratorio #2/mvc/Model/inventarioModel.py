class Inventario:
	
	idInventario = 0
	def __init__(self, registrar, stock, cantidad, tipoMoviento, fecha):
		self.registrar = registrar
		self.stock = stock
		self.cantidad = cantidad
		self.tipoMoviento = tipoMoviento
		self.fecha = fecha
		Inventario.idInventario += 1
		self.id = Inventario.idInventario
		
		
	
	
	#Getters
	def getRegistrar(self):
		return self.registrar
	
	def getStock(self):
		return self.stock
	
	def getCantidad(self):
		return self.cantidad
	
	def getTipoMoviento(self):
		return self.tipoMoviento
	
	def getFecha(self):
		self.fecha
	
	#Setters
	def setRegistrar(self, registrar):
		self.registrar = registrar
	
	def setStock(self, stock):
		self.stock = stock
	
	def setCantidad(self, cantidad):
		self.cantidad = cantidad
	
	def setTipoMoviento(self, tipoMoviento):
		self.tipoMoviento = tipoMoviento
		
	def setPrecio(self, precio):
		self.precio = precio
		
	def mostrarDatos(self):
		return f" Registro : {self.registrar} Stock: {self.stock} Cantidad: {self.cantidad} Tipo de movimiento: {self.tipoMoviento} Precio: {self.precio}"

