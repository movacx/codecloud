def mostrarMensaje(mensaje):
    print(mensaje)
    
def imprimirListados(arreglo):
    # Definimos el ancho de cada columna
    # {index:<ancho} -> El texto se alinea a la izquierda con el espacio indicado
    header = f"{'numero':<8}|{'tipo':<12}|{'tarifa':<12}|{'estado':<12}"
    print(header)
    print("-" * len(header)) # Línea decorativa
    
    for items in arreglo:
        print(f"{items[0]:<8}|{items[1]:<12}|{items[2]:<12}|{items[3]:<12}")
        

