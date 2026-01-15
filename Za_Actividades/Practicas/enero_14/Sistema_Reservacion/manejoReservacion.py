#La noche costara 23.800 colones habitacion sencilla
#La noche costara 31.500 colones habitacion doble
from ObjetoReservacion import Cliente

arregloClientes = []


#--------------------------------   Agregar Cliente --------------------------------------------------
def agregarCliente(nombre_cliente, noches, tipo_habitacion):
    
    if tipo_habitacion == False:
        costoPor_noche = 23800
        costo_total = noches * costoPor_noche
        addClient = Cliente(nombre_cliente, noches, costoPor_noche, tipo_habitacion, costo_total)
    else:
        costoPor_noche = 31500
        costo_total = noches * costoPor_noche
        addClient = Cliente(nombre_cliente, noches, costoPor_noche, tipo_habitacion, costo_total)
    arregloClientes.append(addClient) 
    return addClient

#-----------------------------------  Buscar Cliente  -------------------------------------------------
def buscarNombre(nombre_buscado):
    for items in arregloClientes:
        if items.getNombre() == nombre_buscado:
            return items  
    return -1

def buscarReservacion(numero_reservacion):
    for item in arregloClientes:
        if item.getNum_reservaciones() == numero_reservacion:
            return item
    return "No se encontro ese identificador"

def buscarIndice(indice):
    if indice >= 0 & indice < len(arregloClientes):
        return arregloClientes[indice]
    return -1

#----------------------------------- Eliminar Clientes -----------------------------------------------------------

def eliminarReservacion(numero_reservacion):
    for item in arregloClientes:
        if item.getNum_reservaciones() == numero_reservacion:
            arregloClientes.remove(item)
            return 1
    return -1

#----------------------------------- mostrarObjetos [Todos] -----------------------------------------------------------
def mostrar():
    for item in arregloClientes:
        print(f"Usuarios registrados: ", item.mostrarTodos())
        
#----------------------------------- modificar Clientes -----------------------------------------------------------
def modificarCliente(idReservacion, nuevoNombre):
    for indice in arregloClientes:
        if indice.getNum_reservaciones() == idReservacion:
            indice.setNombre(nuevoNombre)
            return "Nombre ajustado correctamente", indice
    return -1