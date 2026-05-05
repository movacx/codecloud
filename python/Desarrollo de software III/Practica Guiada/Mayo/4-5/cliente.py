import socket

#configuraciones
direccion_ip= "10.35.118.213"
puerto=80

socket_cliente= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket_cliente.connect((direccion_ip, puerto))
socket_cliente.sendall(bytes("Hola, soy un ciente!!", "utf-8"))

while True:
    in_data=socket_cliente.recv(1024)

    print("Desde  el servidor: ", in_data.decode("UTF-8"))
    out_data=input()
    socket_cliente.sendall(bytes(out_data, "UTF-8"))

    if out_data== 'end':
        break

socket_cliente.close()