import threading
import socket

class AtenderCliente(threading.Thread):
    def __init__(self, direccion_cliente, socket_cliente):
        threading.Thread.__init__(self)
        self.socket_cliente = socket_cliente
        self.direccion_cliente = direccion_cliente
        print('Nueva conexion incluida: ', direccion_cliente)

    def run(self):
        while True:
            data = self.socket_cliente.recv(2040)
            mensaje = data.decode()

            if mensaje == 'bye' or not data:
                break

            print('Desde cliente ', mensaje)
            self.socket_cliente.send(bytes(mensaje, 'utf-8'))
        
        self.socket_cliente.close()
        print('Cliente ', self.direccion_cliente, 'desconectado')

direccion_ip = "10.35.118.211"
puerto = 80
    
#163.178.107.97

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
socket_servidor.bind((direccion_ip, puerto))

print('Servidor iniciado')
print('Esperando peticion de clientes.....')


socket_servidor.listen(1)

while True:
    socket_cliente, direccion_cliente = socket_servidor.accept()
    nuevo_hilo = AtenderCliente(direccion_cliente,socket_cliente)

    nuevo_hilo.start()