from View.recursoView import RecursoView

class ControllerRecurso:
    def __init__(self, root, service)->None:
        self.GUI = RecursoView(root, self)
        self.service = service
        self.imprimir_tabla()

    def registrar_recurso(self)->None:
        try:
            cod = self.GUI.codigo.get()
            nom =self.GUI.nombre.get()
            cat=self.GUI.categoria.get()
            cant_dis=self.GUI.cantidad_dispo.get()
            cost_uni=self.GUI.costoUnitario.get()

            exito = self.service.registrarRecurso(cod,nom,cat,int(cant_dis),int(cost_uni))
            if exito:
                self.GUI.mostrar_mensaje('Exito al registrar!')
            else:
                self.GUI.mostrar_advertencia('Ha ocurrido un error')
        except Exception as error:
            self.GUI.mostrar_advertencia(f'Ha ocurrido un error {error}')
            
    def imprimir_tabla(self)->None:
        try:
            self.GUI.limpiar_tabla()
            arreglo = self.service.listarRecursos()
            self.GUI.cargar_tabla(arreglo)
            
        except Exception as error:
            self.GUI.mostrar_advertencia(f'{error}')
