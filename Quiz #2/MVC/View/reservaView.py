def mostrarMensaje(mensaje):
    print(mensaje)

def mostrarReservas(reservas):
    if len(reservas) == 0:
        print("No hay reservas registradas")
    else:
        for rows in reservas:
            print(rows.mostrar_info())