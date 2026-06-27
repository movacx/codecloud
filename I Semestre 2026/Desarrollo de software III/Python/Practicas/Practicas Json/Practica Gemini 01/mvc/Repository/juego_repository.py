import os
import json
from Model.videojuego import Videojuego

# Configuración de rutas al estilo de tu calculadora
dir_data = os.path.dirname(os.path.abspath(__file__))
ARCHIVO = os.path.abspath(os.path.join(dir_data, '..','..','Data', 'juegos.json'))

class JuegoRepository:
    def __init__(self):
        self.juegos = []
        self._load()

    def _load(self):
        if not os.path.exists(ARCHIVO):
            return

        with open(ARCHIVO, 'r', encoding='utf-8') as file:
            data = json.load(file)
            self.juegos = [Videojuego(i['titulo'], i['genero'], i['precio']) for i in data]

    def _save(self):
        data_para_guardar = []
        os.makedirs(os.path.dirname(ARCHIVO), exist_ok=True)

        # Convertimos objetos a diccionarios para que JSON pueda entenderlos
        for items in self.juegos:
            diccionario = items.to_dict()
            data_para_guardar.append(diccionario)

        with open(ARCHIVO, 'w', encoding='utf-8') as file:
            json.dump(data_para_guardar, file, indent=4, ensure_ascii=False)

    def agregar(self, nuevo_juego):
        self.juegos.append(nuevo_juego)
        self._save()

    def get_all(self):
        return self.juegos

    def buscar(self, titulo):
        resultados = []
        for juego in self.juegos:
            if titulo.lower() in juego.titulo.lower():
                resultados.append(juego)
        return resultados