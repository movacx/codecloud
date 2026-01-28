def mostrarMensaje(mensaje):
	print(mensaje)
	
def mostrarDatos(dato):
	return (f"{dato}")


def fileNoFound():
    print('No se encontraron datos! Error al cargar el archivo\n')
            
def mostrarHabitacion(arreglo):
    print()
    print("ID | Rooms Number | Type | Price | State")
    print("-----------------------------------------------")

    for lista in arreglo:
        print(
            str(lista[0]) + "\t| "
            + str(lista[1]) + "\t| "
            + str(lista[2]) + "\t| "
            + str(lista[3]) + "\t| "
	    + str(lista[4]))
        print("-----------------------------------------------")
