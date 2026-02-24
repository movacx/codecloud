from View.ventanaResena import VentanaResena
from Model.ResenaModel import ResenaModel
import Data.baseResenas as dataRes

class ResenaController:
    def __init__(self, root, idUsr, listaProductosComprados):
        self.idCliente = idUsr
        self.listaProductosComprados = listaProductosComprados
        self.GUI = VentanaResena(root, self)
        self.cargarProductos()
#-----------------------------------------------------------------------------------------------------------------------
    #Cargar productos 
    def cargarProductos(self):
        try:
            if self.listaProductosComprados:
                self.GUI.comboProductos["values"] = self.listaProductosComprados
                self.GUI.comboProductos.current(0)
        except Exception as error:
            self.GUI.mostrarError(f"Error al cargar productos: {error}")
#-----------------------------------------------------------------------------------------------------------------------
    #Enviar reseña 
    def enviarResena(self, cantidadEstrellas):
        try:
            idProducto = self.GUI.comboProductos.get()
            if not idProducto:
                self.GUI.mostrarError("Seleccione un producto")
                return

            comentario = self.GUI.txtComentario.get()
            if not comentario:
                comentario = ""

            nuevaResena = ResenaModel(idProducto, self.idCliente, comentario, cantidadEstrellas)
            exito = dataRes.guardarResena(nuevaResena)

            if exito:
                self.GUI.mostrarMensaje("Reseña guardada")
                self.GUI.ventana.destroy()
            else:
                self.GUI.mostrarError("No se pudo guardar la reseña")
        except Exception as error:
            self.GUI.mostrarError(f"Error al enviar reseña: {error}")
            
            