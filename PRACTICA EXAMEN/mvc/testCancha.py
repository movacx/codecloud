from controller.canchaController import CanchaController
def main():
    registroCancha = CanchaController()
    
    while True:
        
        opcion= int(input('''=== SISTEMA DE CENTRO DEPORTIVO AQUAFIT ===
    1. Agregar Cancha
    2. Listar Canchas
    0. Salir
input: ''' ))
        if opcion ==1:
            numero = int(input('numero: '))
            tipo = input('tipo de cancha: ')
            tarifa_hora = int(input('Costo de renta: '))
            estado = input('Estado: ')
            registroCancha.agregarListado(numero,tipo,tarifa_hora,estado)
            pass
        elif opcion== 2:
            registroCancha.listarCanchas()
            pass
        elif opcion == 0:
            break
                
            
        
if __name__=="__main__":
    main()