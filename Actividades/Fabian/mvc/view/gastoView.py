def mostrarMenu():
    print('''
1. Registrar Gasto
2. Ver Gastos(Tabla)
3. ver total Gastado
4. Eliminar Gasto
5. Mostrar precios ordenados
6. Ordenar por mayor''')
    
def mostrarMensaje(mensaje):
    print(mensaje)
    
def mostrarListados(arreglo):
    print('id | Descripcion | monto | categoria | fecha ')
    print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
    for items in arreglo:
        if items:
            print(f'{items[0]},{items[1]},{items[2]},{items[3]},{items[4]}')
            
    