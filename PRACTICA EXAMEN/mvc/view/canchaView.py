def mostrarMensaje(mensaje):
    print(mensaje)
    
def imprimirListados(arreglo):
    print(f'{'numero':<8}|{'tipo':<15}|{'tarifa':<10}|{'estado':<12}')
    print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
    for items in arreglo:
        print(f'{items[0]:<8}|{items[1]:<15}|{items[2]:<10}|{items[3]:<12}')
    print('___________________________________________________')
        
        
        

