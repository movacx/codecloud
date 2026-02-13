from View.huespedesGUI import HuespedGUI
from Model.huespedModel import HuespedModel
import Data.huespedData as data


class HuespedController:

    def __init__(self, root):
        self.ventanaPrincipal = root
        self.gui = HuespedGUI(root, self)
        self.manejoData = data

    def botonClickeado(self, boton):
         if boton == 'x':
              print('el usuario toco un boton')


    def obtenerId(self):
        ultimoId = self.manejoData.verificarUltimoId()
        return ultimoId

    def agregarHuesped(self):
        nombre = self.gui.ent_nombre_huesped.get()
        telefono = self.gui.ent_telefono_huesped.get()

        nuevoRegistro = HuespedModel(self.obtenerId(), nombre, telefono)
        exito = self.manejoData.agregarListado(nuevoRegistro)

        self.gui.cargarDatos(self.obtenerId(), nombre, telefono)

    def cargarDatos():
        pass