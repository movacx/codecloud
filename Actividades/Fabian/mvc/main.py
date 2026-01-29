import view.gastoView as vista

def main():
    x = True

    while x:
        try:
            vista.mostrarMenu()
            op = int(input('input: '))
            
            if op == 1:
                pass
            elif op == 2:
                pass
            elif op == 3:
                pass
            elif op == 4:
                pass
            else:
                vista.mostrarMensaje('Opcion invalida')
        except ValueError:
            vista.mostrarMensaje('Caracteres no validos')

if __name__ == '__main__':
    main()
        
        
        