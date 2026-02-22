from view.CuentasView import ManejoCuentas
from data.baseClientes import DataClientes
from data.baseCuentas import DataCuentas
from model.ModelCuenta import Cuenta
import random

class ManejoCuentaController:
    def __init__(self,root):
        self.GUI = ManejoCuentas(root, self)
        self.dataCliente = DataClientes()
        self.dataCuenta = DataCuentas()
        self.estado = ''
        
    def aperturaDeCuenta(self):
        self.GUI.mostrarMensaje('El sistema le brindara un numero de cuenta unico. \n al finalizar se le brindara el numero de cuenta en pantalla.')
        self.GUI.bloquearBtn()
        self.GUI.desbloquearCampos()
        self.GUI.bloquearNCUENTA()
        self.estado = 'apertura'
            
    def consultarCuenta(self):
        self.estado = 'consulta'
        self.GUI.bloquearBtn()
        self.GUI.bloquearCampos()
        self.GUI.desbloquearDNI()
        self.GUI.mostrarMensaje('Ingrese la identificacion para consultar el estado de cuenta')

    def depositoDeCuenta(self):
        self.estado = 'deposito'
        self.GUI.bloquearBtn()
        self.GUI.desbloquearCampos()
        self.GUI.bloquearDNI()

    def retiroDeCuenta(self):
        self.estado = 'retiro'
        self.GUI.bloquearBtn()
        self.GUI.desbloquearCampos()
        self.GUI.bloquearDNI()

    



    def recibirAceptar(self):
        if self.estado == 'apertura':
            dni = self.GUI.dnitxt.get()
            saldo = self.GUI.montoTxt.get()
            
            
            if not saldo:
                self.GUI.mostrarAdvertencia('El campo monto es obligatorio')
                return
            
            decimal = float(saldo)
            if decimal < 5000:
                self.GUI.mostrarAdvertencia('El monto mínimo es de 5000 colones')
                return
            else:
                nCuenta = self.generarCuentaAleatoria()
                nuevaCuenta = Cuenta(nCuenta, dni, decimal)
                exito = self.dataCuenta.saveCuenta(nuevaCuenta)
                if exito:
                    self.GUI.mostrarMensaje('Cuenta creada correctamente!')
                    self.GUI.bloquearCampos()
                    self.GUI.desbloquearBtn()
                    self.GUI.limpiarCampos()
                    self.estado = ''
                else:
                    self.GUI.mostrarAdvertencia('No se pudo registrar, ha ocurrido un error')
                    self.GUI.bloquearCampos()
                    self.GUI.desbloquearBtn()
                    self.GUI.limpiarCampos()
                    self.estado = ''
                    
        elif self.estado == 'consulta':
            dni = self.GUI.dnitxt.get()
            if not dni:
                self.GUI.mostrarAdvertencia('Debe de ingresar un numero de DNI para continuar')
                return

            arreglo = self.dataCuenta.searchList(dni)
            if not arreglo:
                self.GUI.bloquearCampos()
                self.GUI.desbloquearBtn()
                self.GUI.limpiarCampos()
                self.estado = ''
                self.GUI.mostrarAdvertencia('No se encontraron datos!')
                return
            else:
                self.GUI.cargarTabla(arreglo)
                self.GUI.bloquearCampos()
                self.GUI.desbloquearBtn()
                self.GUI.limpiarCampos()
                self.estado = ''
                return
        elif self.estado == 'deposito':
            cuenta = self.GUI.nCuentatxt.get()
            saldo = self.GUI.montoTxt.get()
            
            arreglo = self.dataCuenta.obtenerSaldo(cuenta)
            if not arreglo:
                self.GUI.bloquearCampos()
                self.GUI.desbloquearBtn()
                self.GUI.limpiarCampos()
                self.estado = ''
                self.GUI.mostrarAdvertencia('No se encontraron datos!')
                return
            else:
                for items in arreglo:
                    numero = items[2]
                nuevoDeposito = float(saldo) + float(numero)
                
                self.dataCuenta.modificar(cuenta, nuevoDeposito)
                imprimir = self.dataCuenta.obtenerSaldo(cuenta)
                self.GUI.cargarTabla(imprimir)
                self.GUI.bloquearCampos()
                self.GUI.desbloquearBtn()
                self.GUI.limpiarCampos()
                self.estado = ''
                return
            
        elif self.estado == 'retiro':
            cuenta = self.GUI.nCuentatxt.get()
            saldo = self.GUI.montoTxt.get()
            
            arreglo = self.dataCuenta.obtenerSaldo(cuenta)
            if not (cuenta and saldo):
                self.GUI.mostrarAdvertencia('Debe de completar todos los campos!')
                return
            
            if not arreglo:
                self.GUI.bloquearCampos()
                self.GUI.desbloquearBtn()
                self.GUI.limpiarCampos()
                self.estado = ''
                self.GUI.mostrarAdvertencia('No existe la cuenta ingresada!')
                return
            else:
                for items in arreglo:
                    numero = items[2]
                nuevoRetiro =  float(numero) - float(saldo)
                if nuevoRetiro < 0:
                    self.GUI.mostrarAdvertencia('Fondos insuficientes, consulte su cuenta bancaria')
                    self.GUI.bloquearCampos()
                    self.GUI.desbloquearBtn()
                    self.GUI.limpiarCampos()
                    self.estado = ''
                    return
                else:
                    self.dataCuenta.modificar(cuenta, nuevoRetiro)
                    imprimir = self.dataCuenta.obtenerSaldo(cuenta)
                    self.GUI.cargarTabla(imprimir)
                    self.GUI.bloquearCampos()
                    self.GUI.desbloquearBtn()
                    self.GUI.limpiarCampos()
                    self.estado = ''
                    return
                
                
    def generarCuentaAleatoria(self):
        numeroCuenta = random.randint(100000,999999)
        return numeroCuenta
    

        

    

            