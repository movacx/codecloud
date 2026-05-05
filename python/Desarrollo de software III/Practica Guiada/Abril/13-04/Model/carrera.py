'''
Modelo principal del juego
Guarda:
    La distancia de la meta
    La lista de corredores
    El ganador
    El estado de la carrera
'''

class Carrera:
    def __init__(self, meta:int = 650):
        self.meta = meta
        self.corredores = []
        self.ganador = None
        self.en_curso = False

    def agregar_corredor(self, corredor):
        self.corredores.append(corredor)

    def reiniciar(self):
        '''
        Reinicia el estado de la carrera para una nueva partida
        '''

        self.ganador =None
        self.en_curso = False
        for corredor in self.corredores:
            corredor.reiniciar()
            