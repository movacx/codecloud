from Controller.controller import Controller
from View.vista import Vista

def main():
    vista = Vista()
    print('Hola mundo')
    vista.mostrar_mensaje('Hola mundo')

if __name__ == '__main__':
    main()