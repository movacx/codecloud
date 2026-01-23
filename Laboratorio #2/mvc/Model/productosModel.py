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
	