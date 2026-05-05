#Esta version de uso basico de socket presenta una unica comunicacion
#entre un cliente y un servidor
import socket
from encodings.utf_16 import encode

direccion_ip = "10.35.118.169"
puerto = 8080

cliente =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#indica que se usara un sistema basico de direccionamiento ipv4
#comunmente usado en la actualidad, otra opcion seria:
#socket.AF_INET6

#La constante socket.SOCKET_STREAM indica que el protocolo de transferencia
#a usar es TCP
#otra posibilidad seria socket.SOCK_DORAM para usar el protocolo UDP

#Conectar el servidor
cliente.connect((direccion_ip, puerto))

#enviar mensaje
cliente.send("Hola servidor".encode())
#para transferir los datos por la red y por el socket ss requiere
#que el texto se convierte a byte, por ello se usa encode.
#por defecto lo codifica a formato UTF-8

#Recibir respuesta
data = cliente.recv(1024)
print("Servidor dice: ", data.decode())

#el recibir los datos se deben Se convertir los bytes a textos

cliente.close()
