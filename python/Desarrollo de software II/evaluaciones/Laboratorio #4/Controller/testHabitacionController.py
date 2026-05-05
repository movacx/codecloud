from View.testHabitacionGUI import HabitacionGUI
from Model.habitacionModel import HabitacionModel
import Data.baseHabitacion as data

class HabitacionController:
    def __init__(self, root):
        self.GUI = HabitacionGUI(root, self)
        self.ventana = root
        
    #----------------------------------------------------------------------------------------------#
    def savelog(self, nombreError):
        try:
            
            data.guardarError(nombreError)
            
        except Exception as error:
            print(f'No se pudo establecer la coneccion con log.txt >> data + controller = {error}')
            
    #----------------------------------------------------------------------------------------------# 
    def ultimoId(self):
        try:
            
            ultimoId = data.validarUltimoId()
            return ultimoId
        
        except Exception as error:
            self.GUI.errorMessage(f'Hubo un error, valide logfile para mas informacion!')
            self.savelog(error)
            
    #----------------------------------------------------------------------------------------------#
    def registrarHabitacion(self):
        try:
        
            ultimaPosicion = self.ultimoId()
            numeroHabitacion = self.GUI.numHabitacionTxt.get()
            tipoHab = self.GUI.tipoHabitacioncbx.get()
            precio = self.GUI.precioTxt.get()
            estado = self.GUI.estadoHabitacioncbx.get()
            if not numeroHabitacion:
                self.GUI.errorMessage("Debe ingresar un numero de habitacion para continuar")
            else:
                nuevaHabitacion = HabitacionModel(ultimaPosicion, numeroHabitacion, tipoHab, precio, estado)
                exito = data.registrarHabitacion(nuevaHabitacion)
            
                if exito:
                    self.GUI.mostrarMensaje('Exito al guardar!')
                else:
                    self.GUI.errorMessage('Hubo un error interno, valide el logfile')
            
        except Exception as error:
            self.GUI.errorMessage(f'No se pudo registrar la Habitacion. \nvalide logfile para mas informacion!')
            self.savelog(error)
    #----------------------------------------------------------------------------------------------#   
    def imprimirHabitaciones(self):
        try:
            self.GUI.limpiarTabla()
            arreglo = data.listarHabitaciones()
            self.GUI.mostrarRegistros(arreglo)

        except Exception as error:
            self.savelog(error)
            self.GUI.errorMessage(f'No se pudo mostrar la informacion. \nvalide logfile para saber mas!')
            
            
    #-----------------------------------Recargar el filtrado de busqueda---------------------------#
    #Parte 1
    def filtrado(self):
        try:

            registroHabitaciones = data.listarHabitaciones()
            
            listaHabitaciones = []
            
            for items in registroHabitaciones:
                listaHabitaciones.append(items[1])
                
            return listaHabitaciones

        except Exception as error:
            self.savelog(error)
            self.GUI.errorMessage(f'No se pudo recargar las habitaciones \nvalide logfile para saber mas!')

    #Parte 2
    def accionFiltrado(self):
        try:
            #Nota para recargar las listas de busquedas tiene que cerrar la ventana de habitacion y volverla abrir para que la lista se recargue no logre hacerlo este es mi limite
            habitacionSeleccionada = self.GUI.busquedalista.get()
            arreglo = data.buscarHabitacionId(habitacionSeleccionada)
            self.GUI.limpiarTabla()
            self.GUI.mostrarRegistros(arreglo)
            
            
            
        except Exception as error:
            self.GUI.errorMessage(f'No se pudo recargar las habitaciones \nvalide logfile para saber mas!')
            self.savelog(error)
        
    #----------------------------------------------------------------------------------------------#
        
    def limpiarInputs(self):
        try:
            
            self.GUI.limpiarCampos()
            self.GUI.limpiarTabla()
            
        except Exception as error:
            self.savelog(error)
            self.GUI.errorMessage(f'Error interno. No se ha podido limpiar los campos. \nPara mas informacion revisa el logfile')

            
    #----------------------------------------------------------------------------------------------#
    
    def eliminarHabitacion(self):
        try:

            seleccion = self.GUI.busquedalista.get()
            habitacion = self.GUI.numHabitacionTxt.get()
            exito = data.eliminarHabitacion(seleccion)
            if exito:
                self.GUI.mostrarMensaje('Borrado exitosamentne!')
            else:
                self.GUI.mostrarMensaje('No se pudo eliminar, valide los campos o la informacion seleccionada!')   

        except Exception as error:
            self.savelog(error)
            self.GUI.errorMessage('Hubo un error. Para mas informacion valide el logfile')
     
    #----------------------------------------------------------------------------------------------#
    def modificarHabitacion(self):
        try:

            seleccion = self.GUI.busquedalista.get()
            estado = self.GUI.estadoHabitacioncbx.get()
            data.modificar(seleccion, estado)

        except Exception as error:
            self.savelog(error)
            self.GUI.errorMessage('Hubo un error. Para mas informacion valide el logfile')

