from view.CreditosView import CreditosGUI
from data.baseCreditos import DataCreditos
from model.ModelCredito import Credito

import random

class ControllerCreditos:
    def __init__(self, root):
        self.GUI = CreditosGUI(root, self)
        self.dataCreditos = DataCreditos()
        self.modo = ''
        
    def solicitarEstado(self):
        self.modo = 'solicitar'
        self.GUI.bloquearBtn()
        self.GUI.prepararSolicitudGUI()
        self.GUI.limpiarCampos()
        self.GUI.mostrarMensaje('Ingrese los datos para el nuevo credito')

    def pagarEstado(self):
        self.modo = 'pagar'
        self.GUI.bloquearBtn()
        self.GUI.prepararPagoGUI()
        self.GUI.limpiarCampos()
        self.GUI.mostrarMensaje('Ingrese el dni y el monto a pagar')

    def consultarEstado(self):
        self.modo = 'consultar'
        self.GUI.bloquearBtn()
        self.GUI.prepararConsultaGUI()
        self.GUI.limpiarCampos()
        self.GUI.mostrarMensaje('Ingrese un dni para consultar el estado')

    def recibirAccion(self):
        if self.modo == 'solicitar':
            dni = self.GUI.txtDni.get()
            montoCredito = self.GUI.txtMontoCredito.get()
            cuotasTotales = self.GUI.txtCantidadCuotas.get()
            
            if not (dni and montoCredito and cuotasTotales):
                self.GUI.mostrarAdvertencia('Debe de completar todos los campos para continuar')
                return

            
            montoFloat = float(montoCredito)

            arreglo = self.dataCreditos.searchList(dni)
            if arreglo:
                for items in arreglo:
                    if items[5] == 'Activo':
                        self.GUI.mostrarAdvertencia('El cliente ya tiene un credito activo')
                        self.botonLimpiarCancelar()
                        return

            ide = self.crearID()
            nuevoCredito = Credito(ide, dni, montoFloat, cuotasTotales, 0, 'Activo')
            exito = self.dataCreditos.saveCredito(nuevoCredito)
            
            if exito:
                self.GUI.mostrarMensaje('Registrado con exito!')
                self.botonLimpiarCancelar()
            else:
                self.GUI.mostrarError('Error al guardar el credito')
                self.botonLimpiarCancelar()
                
        elif self.modo == 'pagar':
            dni = self.GUI.txtDni.get()
            montoAPagar = self.GUI.txtMontoPagar.get()
            
            if not (dni and montoAPagar):
                self.GUI.mostrarAdvertencia('Debe de completar todos los campos para continuar')
                return
                
                
            ingreso = float(montoAPagar)
                
            arreglo = self.dataCreditos.searchList(dni)
            if not arreglo:
                self.GUI.mostrarAdvertencia('No se encontraron datos!')
                self.botonLimpiarCancelar()
                return
            
            creditoActivo = None
            for items in arreglo:
                if items[5] == 'Activo':
                    creditoActivo = items
                    break
                    
            if not creditoActivo:
                self.GUI.mostrarAdvertencia('El cliente no tiene creditos activos')
                self.botonLimpiarCancelar()
                return
            
            montoInicial = float(creditoActivo[2])
            totales = int(creditoActivo[3])
            pagadas = int(creditoActivo[4])
            
            cuotaFija = montoInicial / totales
            cuotasAbonadas = int(round(ingreso / cuotaFija, 0))
            
            if cuotasAbonadas <= 0:
                self.GUI.mostrarAdvertencia(f'El monto es muy bajo. La cuota es de: {round(cuotaFija, 2)}')
                return
            
            nuevasPagadas = pagadas + cuotasAbonadas
            nuevoEstado = 'Activo'
            
            if nuevasPagadas >= totales:
                nuevasPagadas = totales
                nuevoEstado = 'Finalizado'
                self.GUI.mostrarMensaje('Se ha cancelado la totalidad del credito')
            else:
                self.GUI.mostrarMensaje(f'Exito al registrar el pago de {cuotasAbonadas} cuotas')
            
            self.dataCreditos.modificar(dni, nuevasPagadas, nuevoEstado)
            self.cargarTablaCalculada(dni)
            self.botonLimpiarCancelar()

        elif self.modo == 'consultar':
            dni = self.GUI.txtDni.get()
            if not dni:
                self.GUI.mostrarAdvertencia('Debe de ingresar un numero de DNI para continuar')
                return
                
            arreglo = self.dataCreditos.searchList(dni)
            if not arreglo:
                self.GUI.mostrarAdvertencia('No se encontraron datos!')
                self.botonLimpiarCancelar()
                return
            else:
                self.cargarTablaCalculada(dni)
                self.botonLimpiarCancelar()
                self.GUI.mostrarMensaje('Datos encontrados')

    def cargarTablaCalculada(self, dni):
        arreglo = self.dataCreditos.searchList(dni)
        listaTabla = []
        
        for items in arreglo:
            montoOriginal = float(items[2])
            totales = float(items[3])
            pagadas = float(items[4])
            
            cuotaFija = montoOriginal / totales
            deuda = montoOriginal - (pagadas * cuotaFija)
            if deuda < 0: 
                deuda = 0
            
            fila = [items[0], items[1], items[2], items[3], items[4], round(deuda, 2), items[5]]
            listaTabla.append(fila)
            
        self.GUI.cargarTabla(listaTabla)

    def botonLimpiarCancelar(self):
        self.modo = ''
        self.GUI.desbloquearBtn()
        self.GUI.bloquearCampos()
        self.GUI.limpiarCampos()
        
    def crearID(self):
        idgenerado = random.randint(10000,90000)
        return idgenerado