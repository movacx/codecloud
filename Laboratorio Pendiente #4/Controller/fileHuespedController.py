from View.fileHuespedesGUI import HuespedGUI
from Model.huespedModel import HuespedModel
import Data.huespedData as data
from tkinter import messagebox

class HuespedController:

    def __init__(self, root):
        self.ventanaPrincipal = root
        self.vista = HuespedGUI(root, self)

    def errorLogs(self, error):
        try:

            data.guardarError(error)

        except Exception as nombreError:
            self.vista.mostrarMensajes(f'Error Critico No se pudo conectarLogFile con el Controller {nombreError} ')
            self.vista.mensaje(f'{nombreError}')
        

    def obtenerId(self):
        try:

            ultimoId = data.verificarUltimoId()
            return ultimoId
        
        except Exception as error:
            self.errorLogs(f'Hubo un error: {error}')
            self.vista.messageError(error)
            print()


    def agregarHuesped(self):
        try:
            nombre = self.vista.ent_nombre_huesped.get()
            telefono = self.vista.ent_telefono_huesped.get()
            nuevoRegistro = HuespedModel(self.obtenerId(), nombre, telefono)
            exito = data.agregarListado(nuevoRegistro)
            self.vista.cargarNuevoDato(self.obtenerId(), nombre, telefono)

        except Exception as error:
            self.errorLogs(f'IN | AGREGAR |: {error}')
            self.vista.mostrarMensajes(f'Hubo un error, revisa el cuadro de errores')
            self.vista.mensaje(f'IN | AGREGAR |: {error}')

        
    
    def buscarHuesped(self):
        try:

            nombre = self.vista.ent_nombre_huesped.get()
            arreglo = data.searchName(nombre)
            self.vista.limpiarTabla()
            self.vista.cargarDatos(arreglo)
        
        except Exception as error:
            self.errorLogs(f'IN | BUSCAR |: {error}')
            self.vista.mostrarMensajes(f'Hubo un error, revisa el cuadro de errores')
            self.vista.mensaje(f'IN | BUSCAR |: {error}')


    def EliminarHuesped(self):
        try:

            self.vista.limpiarTabla()
            nombre = self.vista.ent_nombre_huesped.get()
            huespedEncontrado = data.searchName(nombre)
            self.vista.cargarDatos(huespedEncontrado)
            respuesta = self.vista.mostrarConfirmacion('Manejo Huesped', '¿Desea continuar?')
            if respuesta:
                data.eliminarLista(nombre)
                self.vista.mostrarMensaje('Eliminado correctamente!')
                self.vista.limpiarTabla()
            else:
                return
        

        except Exception as error:
            self.errorLogs(f'IN | ELIMINAR |: {error}')
            self.vista.mostrarMensajes(f'Hubo un error, revisa el cuadro de errores')
            self.vista.mensaje(f'IN | ELIMINAR |: {error}')

    def cargarHuespedes(self):
        try:

            arreglo = data.listarTodos()
            self.vista.limpiarTabla()
            self.vista.cargarDatos(arreglo)

        except Exception as error:
            self.errorLogs(f'IN | CARGAR |: {error}')
            self.vista.mostrarMensajes(f'Hubo un error, revisa el cuadro de errores')
            self.vista.mensaje(f'IN | CARGAR |: {error}')


    def botonClickeado(self, boton):
        try:
         
         if boton == 'x':
              print('Hola mundo')

        except Exception as error:
            self.errorLogs(f'IN | BOTONCLICKEADO |: {error}')
            self.vista.mostrarMensajes(f'Hubo un error, revisa el cuadro de errores')
            self.vista.mensaje(f'IN | BOTONCLICKEADO |: {error}')
