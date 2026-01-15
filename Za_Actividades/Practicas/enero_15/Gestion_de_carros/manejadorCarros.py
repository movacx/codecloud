from ObjetoCarro import Carro

lista_vehiculos = []

#------------------- Registrar Vehiculos -----------------------------------
def registrarVehiculo(marca,modelo,color,placa):
    registro = Carro(marca,modelo,color,placa)
    lista_vehiculos.append(registro)
    return "Vehiculo registrado!"

#------------------- Buscar Vehiculos -----------------------------------
def buscarVehiculo(identificador):
    for indice in lista_vehiculos:
        if indice.getId() == identificador:
            return indice
    return f"No se encontro vehiculo con el identificador: {identificador}"

def mostrarVehiculos():
    for items in lista_vehiculos:
        print(items.mostrarRegistros())
    return "No hay registros en la base de datos"

#------------------- Eliminar Vehiculos -----------------------------------
def eliminarVehiculo(identificador):
    for items in lista_vehiculos:
        if items.getId() == identificador:
            lista_vehiculos.remove(items)
            return "Eliminado con exito!"
    return "No se encontro en la base de datos"

#------------------- Modificar Vehiculos -----------------------------------
def modificarDatos(id, nuevoDato, opcion):
    vehiculoEncontrado = buscarVehiculo(id)
    if vehiculoEncontrado:
        if opcion == 1:
            vehiculoEncontrado.setMarca(nuevoDato)
            return "Marca modificado con exito!"
        elif opcion == 2:
            vehiculoEncontrado.setModelo(nuevoDato)
            return "Modelo modificado con exito!"    
        elif opcion == 3:
            vehiculoEncontrado.setColor(nuevoDato)
            return "Color modificado con exito!" 
        elif opcion == 4:
            vehiculoEncontrado.setPlaca(nuevoDato)
            return "Placa modificado con exito!"   
    return -1