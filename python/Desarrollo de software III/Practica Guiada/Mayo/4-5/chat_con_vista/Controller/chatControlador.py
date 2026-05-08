class ChatControlador:
    def __init__(self, vista,conexion,nombre):
        self.vista = vista
        self.conexion=vista
        self.nombre=nombre

        self.vista.on_enviar(self.enviar)
        self.conexion.iniciar(self.recibir)

        self.conexion.enviar({
            "tipo":"login",
            "usuario":self.nombre
        })

    def enviar(self):
        texto = self.vista.get_texto()

        if not texto.strip():
            return
        
        self.conexion.enviar({
            "tipo":"mensaje",
            "texto":texto
        })

    def recibir(self, objeto):
        tipo=objeto.get('tipo')
        if tipo == 'mensaje':
            self.vista.mostrar(f'{objeto['usuario']}:{objeto['texto']}')
        elif tipo == 'sistema':

        elif tipo == 'mensaje':
        elif tipo == 'mensaje':
        elif tipo == 'mensaje':