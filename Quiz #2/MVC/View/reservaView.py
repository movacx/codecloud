def mostrarMensaje(mensaje):
    print(mensaje)

def fileNoFound():
    print('No se encontraron datos! Error al cargar el archivo\n')

def mostrarListados(arreglo):
    print('\nID | Nombre          ')
    
    for lista in arreglo:
        if arreglo:
            print(f'{lista[0]}  | {lista[1]}     {lista[2]}')
            print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾') #alt+shit+u+203e enter en linux, windows alt 8254
