from View.testHabitacionGUI import HabitacionGUI
from Model.habitacionModel import HabitacionModel
import Data.baseHabitacion as data

class HabitacionController:
    def __init__(self, root):
        self.GUI = HabitacionGUI(root, self)
        self.ventana = root
        
    
    def savelog(self, nombreError):
        try:
            
            data.guardarError(nombreError)
            
        except Exception as error:
            print(f'No se pudo establecer la coneccion con log.txt >> data + controller = {error}')
            
            #ide, numero, tipo, precio, estado
            
    def ultimoId(self):
        try:
            
            ultimoId = data.validarUltimoId()
            return ultimoId
        
        except Exception as error:
            self.GUI.errorMessage(f'Hubo un error, valide logfile para mas informacion! {error}')
            self.savelog(error)
    
    def registrarHabitacion(self):
        try:
            ultimaPosicion = self.ultimoId()
            numeroHabitacion = self.GUI.numHabitacionTxt.get()
            tipoHab = self.GUI.tipoHabitacioncbx.get()
            precio = self.GUI.precioTxt.get()
            estado = self.GUI.estadoHabitacioncbx.get()
            
            nuevaHabitacion = HabitacionModel(ultimaPosicion, numeroHabitacion, tipoHab, precio, estado)
            exito = data.registrarHabitacion(nuevaHabitacion)
            
            
            
            if exito:
                self.GUI.mostrarMensaje('Exito al guardar!')
            else:
                self.GUI.errorMessage('Hubo un error interno, valide el logfile')
                
            
        except Exception as error:
            self.GUI.errorMessage(f'No se pudo registrar la Habitacion. \nvalide logfile para mas informacion! {error}')
            self.savelog(error)
            
    def imprimirHabitaciones(self):
        try:

            arreglo = data.listarHabitaciones()
            self.GUI.listaHabitaciones.append(arreglo[1])
            self.GUI.mostrarRegistros(arreglo)

        except Exception as error:
            self.savelog(error)
            self.GUI.errorMessage(f'No se pudo mostrar la informacion. \nvalide logfile para saber mas! {error}')

    def filtrado(self):
        #-----------------------------------Recargar el filtrado de busqueda---------------------------#
        registroHabitaciones = data.listarHabitaciones()
        
        listaHabitaciones = []
        
        for items in registroHabitaciones:
            listaHabitaciones.append(items[2])
            
        return listaHabitaciones
            
    
        
        
        
        