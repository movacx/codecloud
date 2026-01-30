#from Model.socioModel import Socio
from model.socioModel import Socio
import view.socioView as vista
#import View.socioView as vista
#import Data.baseSocio as baseSocio
import data.baseSocio as base

class SocioController:
    
    def __init__(self):
        pass
        
#-------------------------------------------------------------------------#
#Registrar socio
    def registrarSocio(self,nombre, telefono):
        objetoSocio = Socio(0,nombre, telefono)
        registrar = baseSocio.registrarSocio(objetoSocio)
        vista.mostrarMensaje("Agregado con exito")
#-------------------------------------------------------------------------#       

        



