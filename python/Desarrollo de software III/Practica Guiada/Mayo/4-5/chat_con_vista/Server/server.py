import socket
import threading
import json
from server.gestor_usuarios import GestorUsuarios
import struct


class ServidorChat:
    def __init__(self, direccion_ip = "10.35.118.211", puerto="80"):
        self.direccion_ip = direccion_ip
        self.puerto = puerto
        self.socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.clientes=[] #sockets
        self.sockets_a_sessiones = {}
        self.lock=threading.Lock
        self.gestor = GestorUsuarios()

    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-#
    def enviar_objeto(self, el_socket, objeto):
        data = json.dumps(objeto).encode()

        el_socket.send(struct.pack('!I', len(data)))
        el_socket.sendall(data)

    def recibir_objeto(self, el_socket):
        data = el_socket.recv(4)
        if not data:
            return None
        

