import json
import os
from Model.videojuego import Videojuego
class JuegoRepository:
    def __init__(self, archivo = 'juegos.json'):
        self.archivo = archivo
        self.juegos = []
        self._load()

    def _load(self):
        #1. Verificamos si el archivo existe
        if not os.path.exists(self.archivo):
            return
        #2. Abrimos y cargamos el JSON
        with open(self.archivo, 'r', encoding = 'utf-8') as file:
            data = json.load(file)
        #3. Convertimos cada diccionario de vuelta a objeto VideoJuego
        for item in data:
            nuevo_juego = Videojuego(item['titulo'], item['genero'], item['precio'])
            self.juegos.append(nuevo_juego)

    def _save(self):
        #Convertimos la lista de objetos a una lista de diccionarios
        data_para_guardar = []
        for items in self.juegos:
            diccionario = items.to_dict()
            data_para_guardar.append(diccionario)

        with open(self.archivo, 'w', encoding= 'utf-8') as file:
            json.dump(data_para_guardar, file, indent=4, ensure_ascii=False)

    def agregar(self, juego):
        self.juegos.append(juego)
        self._save()
