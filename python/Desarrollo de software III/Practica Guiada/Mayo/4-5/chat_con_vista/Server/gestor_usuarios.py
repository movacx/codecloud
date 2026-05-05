import uuid

class GestorUsuarios:
    '''Clase encargada de la gestion de usuarios del sistema, no depende de socket ni de la red
    maneja sesiones mediante  IDs unicos '''

    def __init__(self):
        #Diccionario: Session_id -> nombre_usuario
        self._usuarios={}

    def crear_session(self, nombre):
        '''
        Crea una nueva sesion para un usuario
        '''

        session_id=str(uuid.uuid4())

        self._usuarios[session_id]=nombre
        return session_id
    
    def eliminar_session(self, session_id):
        return self._usuarios.pop(session_id)
    
    def obtener_nombre(self, session_id):
        return self._usuarios.get(session_id)
    
    def listar(self):
        return list(self._usuarios.values())
    
    def existe(self, nombre):
        return nombre in self._usuarios.values()
    d