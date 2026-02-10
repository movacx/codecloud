def mostrarMensaje(mensaje):
    print(mensaje)

def mostrarListados(arreglo):
    print('\nID  | Habitación | Huésped | Entrada      | Salida')
    print('-' * 60)
    
    for lista in arreglo:
        if lista: 
            print(f'{lista[0]:<3} | {lista[1]:<10} | {lista[2]:<7} | {lista[3]:<12} | {lista[4]}')
            print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾') 

def fileNoFound():
    print('No se encontraron datos! Error al cargar el archivo\n')