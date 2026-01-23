class Inventario(Producto):
	
	idInventario = 0
	def __init__(self, stock, cantidad, tipoMoviento, fecha):
		super().__init__(stock, cantidad, tipoMoviento, fecha)
		Inventario.idInventario += 1
		self.id = Inventario.idInventario


