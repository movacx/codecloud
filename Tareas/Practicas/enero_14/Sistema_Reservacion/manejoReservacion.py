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
    
def buscarID(indice):
    if indice >= 0 and indice < len(arregloClientes):
        return arregloClientes[indice]
    else:
        return "Posicion invalida"


    
def buscar(usuarioNombre):
    indice_encontrado = -1
    contador = 0
    
    for obj_persona in arregloClientes:
        # 1. Obtenemos el nombre usando el objeto actual del ciclo (obj_persona)
        # 2. Usamos () porque es una función
        nombre_actual = obj_persona.getNombre() 
        
        # Comparamos
        if nombre_actual == usuarioNombre:
            indice_encontrado = contador
            break 
        
        contador = contador + 1
        
    return indice_encontrado