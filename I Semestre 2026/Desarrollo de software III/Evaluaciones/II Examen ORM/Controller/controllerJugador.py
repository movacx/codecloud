
from View.ventana_jugador import PlayerWindow
from Service.service_jugador import JugadorService


class ControllerJugador:
    def __init__(self, root):
        self.service = JugadorService()
        self.GUI = PlayerWindow(self, root)
    # =-=-=-=-=-=-==-=--=-=-=-=-==--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=--==--==-=--==--==-=-=-=-=-=--=-=-=-=-==--=-=-=-=-=-=-=-==--=-=-=-=-=-==--=-=#
    def registrar_jugador(self):
        try:
            identificacion = self.GUI.entry_id.get()
            nombre = self.GUI.entry_nombre.get()
            correo = self.GUI.entry_correo.get()
            pais = self.GUI.entry_pais.get()

            #compara esto de abajo
            exito = self.service.agregar(identificacion, nombre, correo, pais)
            if exito:
                self.GUI.mostrar_advertencia('Registrado correctamente!')
                print('Registrado correctamente!')
        except Exception as error:
            self.GUI.mostrar_advertencia(f'{error}')

    # =-=-=-=-=-=-==-=--=-=-=-=-==--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=--==--==-=--==--==-=-=-=-=-=--=-=-=-=-==--=-=-=-=-=-=-=-==--=-=-=-=-=-==--=-=#
    def listar_jugados(self):
        try:
            self.GUI.limpiar_tabla()
            objeto = self.service.mostrar()
            self.GUI.cargar_tabla(objeto)
        except Exception as error:
            self.GUI.mostrar_advertencia(f'{error}')
    # =-=-=-=-=-=-==-=--=-=-=-=-==--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=--==--==-=--==--==-=-=-=-=-=--=-=-=-=-==--=-=-=-=-=-=-=-==--=-=-=-=-=-==--=-=#
    def buscar_jugador(self):
        try:
            self.GUI.limpiar_tabla()
            identificacion = self.GUI.entry_id.get()
            objeto = self.service.buscar(identificacion)
            print(objeto)
            self.GUI.insertar_tabla(objeto)
        except Exception as error:
            self.GUI.mostrar_advertencia(f'{error}')
    # =-=-=-=-=-=-==-=--=-=-=-=-==--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=--==--==-=--==--==-=-=-=-=-=--=-=-=-=-==--=-=-=-=-=-=-=-==--=-=-=-=-=-==--=-=#
    def buscar_pais(self):
        try:
            self.GUI.limpiar_tabla()
            pais = self.GUI.entry_pais.get()
            objeto = self.service.filtrar_pais(pais)
            self.GUI.insertar_tabla(objeto)
        except Exception as error:
            self.GUI.mostrar_advertencia(f'{error}')



