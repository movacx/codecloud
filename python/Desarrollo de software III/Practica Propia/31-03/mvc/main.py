from Controller.estudianteController import Controller

def main():
    
    manejoController = Controller()
    

    manejoController.listar()
    
    carnet = input('Ingrese el numero de carnet: ')
    nombre = input('Ingrese el nombre: ')
    apellido = input('Ingrese el apellido: ')
    carrera = input('Ingrese la carrera: ')
    


    manejoController.agregarEstudiante(carnet, nombre, apellido, carrera)

    

if __name__ == '__main__':
    main()

    