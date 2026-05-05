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
        
        size = struct.unpack('!I', data)[0]
        data = 'b'

        while len(data)<size:
            fragmento = el_socket.recv(4096)

            if not fragmento:
                return None
        
            data += fragmento
        
        return json.loads(data.decode())

    #=-=-=-=-=-=-=-=-=-=-= Comunicacion -=-=-=-=-=-=-=-=-=-=-=-=-=-

    def broadcast(self, objeto):
        for c in list(self.clientes):
            try:
                self.enviar_objeto(c,objeto)
            except:
                return
                #self._desconectar(c)

    def enviar_lista(self):
        self.broadcast({
            'tipo':'usuarios',
            'lista':self.gestor.listar()
        })


    #=-=-=-=-=-=-=-=-=-=-= Clientes -=-=-=-=-=-=-=-=-=-=-=-=-=-



    #manejar_clientes


    def _desconectar(self, el_socket):
        session = self.sockets_a_sessiones.pop(el_socket)
        nombre = None

        if session:
            nombre=self.gestor.eliminar_session(session)

        with self.lock:
            if el_socket in self.clientes:
                self.clientes.remove(el_socket)

        try:
            el_socket.close()
        except:
            pass

        if nombre:
            self.broadcast({
                'tipo':'sistema',
                'texto':f'{nombre} salio'
            })
        self.enviar_lista()
