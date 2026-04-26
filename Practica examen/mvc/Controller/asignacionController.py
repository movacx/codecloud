from View.asignacionView import AsignacionView

class AsignacionController:
    def __init__(self, root, service)->None:
        self.GUI = AsignacionView(root, self)
        self.service = service
        self.imprimir_tabla()

    def nueva_asignacion(self)->None:
        try:
            cod = self.GUI.codigo.get()
            ben = self.GUI.beneficiario.get()
            rec = self.GUI.recurso.get()
            cant = self.GUI.cantidad_entregada.get()
            fech = self.GUI.fecha.get()
            res = self.GUI.responsable.get()

            exito = self.service.agregar(cod,ben,rec,int(cant),fech,res)
            if exito:
                if exito:
                    self.GUI.mostrar_mensaje('Exito al registrar!')
                else:
                    self.GUI.mostrar_advertencia('Ha ocurrido un error')

        except Exception as error:
            self.GUI.mostrar_advertencia('Ha ocurrido un error')
            
            
    def imprimir_tabla(self)->None:
        try:
            arreglo = self.service.listarAsignaciones()
            self.GUI.cargar_tabla(arreglo)
            
        except Exception as error:
            self.GUI.mostrar_advertencia(f'{error}')