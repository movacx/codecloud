from view.UsuariosView import RegistroCuentas
from data.baseClientes import DataClientes
from model.ModelCliente import Cliente

class CuentaController:
    def __init__(self, root):
        self.data = DataClientes()
        self.GUI = RegistroCuentas(root, self)
        
        
    def saveLog(self, error):
        try:
            
            self.data.savelog(error)
            
        except Exception as error:
            self.GUI.dialogoError(error)
    
    def agregarCuenta(self):
        try:
            
            dni = self.GUI.dniTxt.get()
            nombre = self.GUI.nombreTxt.get()
            apellido = self.GUI.apellidoTxt.get()
            email = self.GUI.emailTxt.get()


            if not (dni and nombre and apellido and email):
                self.GUI.mostrarAdvertencia('Debe de completar todos los campos para continuar')
                return
            else:
                nuevoRegistrobj = Cliente(dni,nombre,apellido,email)
                
                exito = self.data.saveCliente(nuevoRegistrobj)
                if exito:
                    self.GUI.actualizarTabla(dni, nombre, apellido, email)
                    self.GUI.mostrarMensaje('Registrado con exito!')
                    return
                else:
                    self.GUI.mostrarError('No se pudo registrar!')
                    return
                
        except Exception as error:
            self.GUI.dialogoError(f'Hubo un problema interno. {error}')
            self.saveLog(error)
            
            
    def mostrarRegistros(self):
        try:
            self.GUI.limpiarTabla()
            arreglo = self.data.list()
            if not arreglo:
                self.GUI.mostrarAdvertencia('No se encontraron datos!')
            else:
                self.GUI.cargarTabla(arreglo)
                
            
        except Exception as error:
            self.GUI.dialogoError(f'Hubo un problema interno. {error}')
            self.saveLog(error)
            
    def limpiarTodo(self):
        try:
            
            self.GUI.limpiarCampos()
            #self.GUI.limpiarTabla()
            self.GUI.desbloquearPrimerCampo()
            self.GUI.desbloquearCampos()
            
        except Exception as error:
            self.saveLog(error)
            self.GUI.dialogoError(f'Hubo un problema interno. {error}')
            
    def buscarCliente(self):
        try:
            dni = self.GUI.dniTxt.get()
            self.GUI.limpiarTabla()
            arreglo = self.data.searchList(dni)
            if not arreglo:
                self.GUI.mostrarAdvertencia('No se encontraron datos!')
            else:
                self.GUI.cargarTabla(arreglo)
                
            
        except Exception as error:
            self.GUI.dialogoError(f'Hubo un problema interno. {error}')
            self.saveLog(error)
            
            
    def modificarCliente(self):
        try:
            
            dni = self.GUI.dniTxt.get()
            nombre = self.GUI.nombreTxt.get()
            apellido = self.GUI.apellidoTxt.get()
            email = self.GUI.emailTxt.get()
            
            if not (dni and nombre and apellido and email):
                self.GUI.mostrarAdvertencia('Debe de completar los compos antes de continuar')
                return
            
            self.GUI.bloquearPrimerCampo()
            self.GUI.limpiarTabla()
            
            
            
            si_no = self.GUI.confirmarAccion() #Llamo el messagebox askyesno
            if si_no: #si es true me deberia modificar
                exito = self.data.modificar(dni, nombre, apellido, email) #llama al data y modifica
                arreglo = self.data.searchList(dni) #busco el que se acaba de modificar
                self.GUI.cargarTabla(arreglo) #cargo en la tabla
                if exito: #Si la modificacion fue exitosa
                    self.GUI.mostrarMensaje('Exito al modificar!')
                    return
                    
                else: #sino 
                    self.GUI.mostrarAdvertencia('No se encontraron Datos')
                    return
            else:
                return
            
            
            
        except Exception as error:
            self.GUI.dialogoError(f'Hubo un problema interno. {error}')
            self.saveLog(error)
            
    def eliminarCliente(self):
        try:
            
            dni = self.GUI.dniTxt.get()
            self.GUI.bloquearCampos()
            self.GUI.desbloquearPrimerCampo()
            self.GUI.limpiarTabla()
            
            arreglo = self.data.searchList(dni)
            self.GUI.cargarTabla(arreglo)
            
            si_no = self.GUI.confirmarAccion()
            if si_no:
                
                exito = self.data.deleteDNI(dni)
                if exito:
                    self.GUI.limpiarTabla()
                    self.GUI.mostrarMensaje('Exito al Eliminar!')
                    
                    return
                    
                else: 
                    self.GUI.mostrarAdvertencia('No se encontraron Datos')
                    return
            else:
                return
            
        except Exception as error:
            self.GUI.dialogoError(f'Error interno {error}')