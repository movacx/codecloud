def mostrarMensaje(mensaje):
	print(mensaje)
	
def mostrarDatos(dato):
	print (dato)
	
	
def mostrarGastos(arreglo):
	for item in arreglo:
		print (f"ID: {item[0]}, Descripcion: {item[1]} Monto:{item[2]} Categoria: {item[3]}Fecha: {item[4]}")
		
