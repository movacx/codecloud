'''
Modelo que representa a un corredor dentro del juego guarda su nombre, color y posicion actual
'''

class Corredor:
    def __init__(self, nombre: str, color: str, posicion: float):
        self.nombre = nombre
        self.color = color
        self.posicion = 0

    def reiniciar(self):
        'Vuelve a la posicion incial'
        self.posicion = 0