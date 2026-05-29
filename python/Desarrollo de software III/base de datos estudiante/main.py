from controller.estudiantes_controller import EstudianteController

def main():
    controller = EstudianteController()
    controller.mostrar_menu()

#Recordatorio: La siguiente instruccion permite que el programa solo inicie cuando se ejecuta este archivo
#El programa solo inicie cuando se ejecuta este archivo, si el archivo fuer aimportado desde otro modulo
#main() no se ejecutara automaticamente


if __name__ == '__main__':
    main()