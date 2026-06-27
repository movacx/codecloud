from View.ventana_juego import GameWindow
from Service.service_videoJuego import VideoJuegoService
class ControllerVideoJuego:
    def __init__(self, root):
        self.service = VideoJuegoService()
        self.GUI = GameWindow(self, root)
    # =-=-=-=-=-=-==-=--=-=-=-=-==--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=--==--==-=--==--==-=-=-=-=-=--=-=-=-=-==--=-=-=-=-=-=-=-==--=-=-=-=-=-==--=-=#
    def registrar_videoJuego(self):
        try:
            codigo = self.GUI.entry_codigo.get()
            titulo = self.GUI.entry_titulo.get()
            desarrollador = self.GUI.entry_desarrollador.get()
            categoria = self.GUI.entry_categoria.get()
            licencias_disponibles = self.GUI.entry_stock.get()

            exito = self.service.agregar(codigo, titulo, desarrollador, categoria, int(licencias_disponibles))
            if exito:
                self.GUI.mostrar_mensaje('Registrado correctamente!')
                print('Registrado correctamente!')
        except Exception as error:
            self.GUI.mostrar_advertencia(f'{error}')
    # =-=-=-=-=-=-==-=--=-=-=-=-==--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=--==--==-=--==--==-=-=-=-=-=--=-=-=-=-==--=-=-=-=-=-=-=-==--=-=-=-=-=-==--=-=#
    def listar_video_juegos(self):
        try:
            self.GUI.limpiar_tabla()
            objeto = self.service.mostrar()
            self.GUI.cargar_tabla(objeto)
        except Exception as error:
            self.GUI.mostrar_advertencia(f'{error}')
    # =-=-=-=-=-=-==-=--=-=-=-=-==--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=--==--==-=--==--==-=-=-=-=-=--=-=-=-=-==--=-=-=-=-=-=-=-==--=-=-=-=-=-==--=-=#
    def buscar_video_id(self):
        try:
            self.GUI.limpiar_tabla()
            codigo = self.GUI.entry_codigo.get()
            objeto = self.service.buscar(codigo)
            print(objeto)
            self.GUI.insertar_tabla(objeto)
        except Exception as error:
            self.GUI.mostrar_advertencia(f'{error}')
    # =-=-=-=-=-=-==-=--=-=-=-=-==--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=--==--==-=--==--==-=-=-=-=-=--=-=-=-=-==--=-=-=-=-=-=-=-==--=-=-=-=-=-==--=-=#
    def buscar_categoria(self):
        try:
            self.GUI.limpiar_tabla()
            categoria = self.GUI.entry_categoria.get()
            objeto = self.service.filtrar_categoria(categoria)
            self.GUI.insertar_tabla(objeto)
        except Exception as error:
            self.GUI.mostrar_advertencia(f'{error}')