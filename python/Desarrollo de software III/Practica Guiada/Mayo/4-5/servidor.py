import threading
import Thread

class AtenderCliente(threading.Thread):
    def __init__(self,direccion_cliente,socket_cliente):
        threading.Thread.__init__(self)
        self.socket_cliente=socket_cliente
        print('')

        