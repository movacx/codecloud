from Model import baseProducto
def registrarProducto(nombre, categoria, precio, stock):
	if precio <= 0:
		return "Precio invalido"
	if stock < 0:
		return "Stock invalido"
	
	
	Producto.guardarProducto(nombre, categoria, precio, stock)
	return "Producto registrado"