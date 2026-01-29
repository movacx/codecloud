from controller.gastoController import GastoController

def main():
    manejoGasto=GastoController()
    
    while True:
        opcion= int(input("1 registrar n/ 2 listar 3 eliminar 4 total gastado" ))
        if opcion ==1:
            descripcion= input("Descripcio: ")
            monto= int(input("monto: "))
            categoria= input("categoria: ")
            fecha= input("fecha: ")
            manejoGasto.registrarGasto(descripcion, monto, categoria, fecha)
            pass
        elif opcion== 2:
            manejoGasto.listar()
        elif opcion == 3:
            id=int(input("ingrese id a eliminar: "))
            manejoGasto.eliminar(id)   
        elif opcion == 4:
            total=manejoGasto.totalGastado()
            print("El total gastado es: ",total)
                
            
        
if __name__=="__main__":
    main()