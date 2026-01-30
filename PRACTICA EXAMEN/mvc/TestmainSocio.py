#from Controller.socioController import SocioController
from controller.socioController import SocioController
#import View.socioView as vista
import view.socioView as vista
def main():
    manejadorController = SocioController()
    while True:
        opcion= int(input('''=== SISTEMA DE CENTRO DEPORTIVO AQUAFIT ===
1. Registrar socio
2. Buscar por nombre
3. Listar socios
5. Salir
Input: ''' ))
        
        if opcion ==1:
            nombre = input("Digite el nombre del socio: " )
            telefono = int(input("Digite el telefono: "))
            manejadorController.registrarSocio(nombre, telefono)
        elif opcion== 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            pass
                
            
        
if __name__=="__main__":
    main()

