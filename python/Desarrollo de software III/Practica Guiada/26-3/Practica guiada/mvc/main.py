'''Archivo principal del sistema
Respondabilidad:
    -iniciar aplicacion
    -crear la vista y el controlador
    -mantener el ciclo principal del menu

Relacion SOLID
SRP: Este archivo solamente iniciay controla el ciclo general del programa
No tiene logica de negocio'''

def main() -> None:
    '''
    Funcion principal del sistema
    ejecuta el men en bucle has que el usuario decida salir
    return
    '''

    vista = VistaConsola()