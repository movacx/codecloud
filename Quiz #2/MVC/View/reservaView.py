class ReservaView:

    def mostrar_reservas(self, reservas):
        if not reservas:
            print("No hay reservas registradas")
        else:
            for rows in reservas:
                print(rows.mostrar_info())

    def mostrar_mensaje(self, mensaje):
        print(mensaje)
