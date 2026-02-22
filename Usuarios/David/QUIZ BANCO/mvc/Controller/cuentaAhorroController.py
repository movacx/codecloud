import tkinter as tkGUI
from tkinter import messagebox
from View.cuentaAhorroGUI import CuentaAhorroGUI
import data.baseCuenta as data
from Model.cuentaAhorroModel import CuentaAhorro

class CuentaAhorroController():
    def __init__(self, root):
        self.ventana = root
        self.GUI = CuentaAhorroGUI(root, self)

    def abrirCuentaAhorro(self):
        numeroCuenta = self.GUI.entradaNumeroCuenta.get()
        dniCliente = self.GUI.entradaDniCliente.get()
        saldo = self.GUI.entradaSaldo.get()
        interesAnual = self.GUI.entradaInteresAnual.get()

        if saldo == "":
            saldo = "0"

        if interesAnual == "":
            interesAnual = "0"

        nuevaCuenta = CuentaAhorroModel(numeroCuenta, dniCliente, float(saldo), float(interesAnual))
        resultado = data.registrarCuenta(nuevaCuenta)

        if resultado:
            messagebox.showinfo("Info", "Cuenta de ahorro creada correctamente")
            self.listarCuentas()
        else:
            messagebox.showinfo("Info", "No se pudo crear (Numero de cuenta repetido o error)")

    def listarCuentas(self):
        arreglo = data.listarCuentas()
        self.GUI.limpiarTabla()
        self.GUI.actualizarTabla(arreglo)

    def buscarCuenta(self):
        numeroCuenta = self.GUI.entradaNumeroCuenta.get()
        encontrado = data.buscarCuentaPorNumero(numeroCuenta)
        self.GUI.limpiarTabla()
        self.GUI.actualizarTabla(encontrado)

    def depositar(self):
        numeroCuenta = self.GUI.entradaNumeroCuenta.get()
        monto = self.GUI.entradaMonto.get()

        if monto == "":
            messagebox.showinfo("Info", "Debe ingresar un monto")
            return

        cuentaEncontrada = data.buscarCuentaPorNumero(numeroCuenta)

        if len(cuentaEncontrada) == 0:
            messagebox.showinfo("Info", "Cuenta no encontrada")
            return

        saldoActual = float(cuentaEncontrada[0][3])
        saldoNuevo = saldoActual + float(monto)

        actualizado = data.actualizarSaldo(numeroCuenta, saldoNuevo)

        if actualizado:
            messagebox.showinfo("Info", "Deposito aplicado correctamente")
            self.buscarCuenta()
        else:
            messagebox.showinfo("Info", "No se pudo actualizar el saldo")

    def retirar(self):
        numeroCuenta = self.GUI.entradaNumeroCuenta.get()
        monto = self.GUI.entradaMonto.get()

        if monto == "":
            messagebox.showinfo("Info", "Debe ingresar un monto")
            return

        cuentaEncontrada = data.buscarCuentaPorNumero(numeroCuenta)

        if len(cuentaEncontrada) == 0:
            messagebox.showinfo("Info", "Cuenta no encontrada")
            return

        saldoActual = float(cuentaEncontrada[0][3])
        montoRetiro = float(monto)

        if montoRetiro > saldoActual:
            messagebox.showinfo("Info", "Fondos insuficientes")
            return

        saldoNuevo = saldoActual - montoRetiro
        actualizado = data.actualizarSaldo(numeroCuenta, saldoNuevo)

        if actualizado:
            messagebox.showinfo("Info", "Retiro aplicado correctamente")
            self.buscarCuenta()
        else:
            messagebox.showinfo("Info", "No se pudo actualizar el saldo")

    def aplicarInteres(self):
        numeroCuenta = self.GUI.entradaNumeroCuenta.get()

        cuentaEncontrada = data.buscarCuentaPorNumero(numeroCuenta)

        if len(cuentaEncontrada) == 0:
            messagebox.showinfo("Info", "Cuenta no encontrada")
            return

        saldoActual = float(cuentaEncontrada[0][3])
        interesAnual = float(cuentaEncontrada[0][4])

        saldoNuevo = saldoActual + (saldoActual * interesAnual)

        actualizado = data.actualizarSaldo(numeroCuenta, saldoNuevo)

        if actualizado:
            messagebox.showinfo("Info", "Interes aplicado correctamente")
            self.buscarCuenta()
        else:
            messagebox.showinfo("Info", "No se pudo aplicar el interes")