from Model import productosModel as model
class ProductoController:
	#Constructor
	def _init__(self):
		self.listaProducto= []

	#Registrar producto 
	def registrarProducto(nombre, categoria, precio, stock):
		if precio <= 0:
			return "Precio invalido"
		if stock < 0:
			return "Stock invalido"
		
		
		model.guardarProducto(nombre, categoria, precio, stock)
		return "Producto registrado"

	#Actualizar Producto 
	def actualizarProducto(id, nombre, categoria, precio, stock):
		if model.buscarProducto(id) is None:
			return "Producto no existe"

		model.modificarProducto(id, nombre, categoria, precio, stock)
		return "Producto actualizado"
	
	#Eliminar Producto
	def eliminarProducto(id):
		model.eliminarProductos(id)
		return "Producto eliminado"