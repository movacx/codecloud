from View.personaView import PersonView

class ControladorPersona:
    def __init__(self, root, service):
        self.GUI = PersonView(root, self)
        self.service = service

    #id, nombre, comunidad, cantidadIntegrantes, prioridadSocial
        
    def registrar_persona(self):
        try:
            id = self.GUI.id.get()
            nom = self.GUI.nombre.get()
            com = self.GUI.comunidad.get()
            cant_integ = self.GUI.cantidad_integrantes.get()
            soc = self.GUI.opcion_combo.get() #Priori social

            exito = self.service.registrar(id,nom,com,cant_integ,soc)
            if exito:
                self.GUI.mostrar_mensaje('Exito al registrar!')
            else:
                self.GUI.mostrar_advertencia('Ha ocurrido un error')
            
        except Exception as error:
            self.GUI.mostrar_advertencia(f'{error}')
            
            
    def imprimir_tabla(self):
        try:
            arreglo = self.service.mostrar_beneficiarios()
            self.GUI.cargar_tabla(arreglo)
            
        except Exception as error:
            self.GUI.mostrar_advertencia(f'{error}')