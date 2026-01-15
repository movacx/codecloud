#La noche costara 23.800 colones habitacion sencilla
#La noche costara 31.500 colones habitacion doble
from ObjetoReservacion import Cliente

arregloClientes = []

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
    
def buscarCliente(posicion):
    posicion =+ 1
    return arregloClientes[posicion]
    
