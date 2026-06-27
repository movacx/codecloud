
def mostrar_programa(vista,estudiante,equipo,categoria,):
    while(True):
        opcion = vista.menu_principal()
        if opcion == 1:
            menu_estudiante(estudiante)
        elif opcion == 2:
            menu_equipos(equipo)
        elif opcion == 3:
            menu_categorias(categoria)
        elif opcion == 4:
            pass
        elif opcion == 5:
            break
        else:
            vista.mostrar_mensaje('Opcion invalida')

def menu_estudiante(controller):
    controller.mostrar_estudiantes()

def menu_equipos(controller):
    controller.mostrar_equipos()

def menu_categorias(controller):
    controller.mostrar_categorias()
