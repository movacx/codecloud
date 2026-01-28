def mostrarMensaje(mensaje):
    print(mensaje)

def mostrarListados(arreglo):
    # Encabezado para 5 columnas
    print('\nID  | Habitación | Huésped | Entrada      | Salida')
    print('-' * 60)
    
    for lista in arreglo:
        if lista: 
            # Imprimimos los 5 datos alineados
            # {lista[0]} = ID Reserva
            # {lista[1]} = Numero Habitacion
            # {lista[2]} = ID Huesped
            # {lista[3]} = Fecha Entrada
            # {lista[4]} = Fecha Salida
            print(f'{lista[0]:<3} | {lista[1]:<10} | {lista[2]:<7} | {lista[3]:<12} | {lista[4]}')
            
            # Tu subrayado especial
            print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾') 

def fileNoFound():
    print('No se encontraron datos! Error al cargar el archivo\n')