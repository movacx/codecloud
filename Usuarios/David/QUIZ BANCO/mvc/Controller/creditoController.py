import tkinter as tkGUI
from tkinter import messagebox
from View.creditoGUI import CreditoGUI
import data.baseCredito as data
from Model.creditoModel import CreditoModel


class CreditoController():
    def __init__(self, root):
        self.ventana = root
        self.GUI = CreditoGUI(root, self)

    def solicitarCredito(self):
        dniCliente = self.GUI.entradaDniCliente.get()
        montoPrestado = self.GUI.entradaMontoPrestado.get()
        cuotasTotales = self.GUI.entradaCuotasTotales.get()

        activos = data.listarCreditosActivosPorDni(dniCliente)

        if len(activos) > 0:
            messagebox.showinfo("Info", "El cliente ya tiene un credito activo")
            return

        nuevoCredito = CreditoModel(0, dniCliente, float(montoPrestado), int(cuotasTotales), 0, "Activo")

        resultado = data.registrarCredito(nuevoCredito)

        if resultado:
            messagebox.showinfo("Info", "Credito registrado correctamente")
            self.listarCreditos()
        else:
            messagebox.showinfo("Info", "No se pudo registrar el credito")

    def listarCreditos(self):
        arreglo = data.listarCreditos()
        self.GUI.limpiarTabla()
        self.GUI.actualizarTabla(arreglo)

    def buscarCredito(self):
        idCredito = self.GUI.entradaIdCredito.get()
        encontrado = data.buscarCreditoPorId(idCredito)
        self.GUI.limpiarTabla()
        self.GUI.actualizarTabla(encontrado)

    def pagarCuota(self):
        idCredito = self.GUI.entradaIdCredito.get()
        montoPago = self.GUI.entradaMontoPago.get()

        creditoEncontrado = data.buscarCreditoPorId(idCredito)

        if len(creditoEncontrado) == 0:
            messagebox.showinfo("Info", "Credito no encontrado")
            return

        cuotasTotales = int(creditoEncontrado[0][3])
        cuotasPagadas = int(creditoEncontrado[0][4])
        estado = creditoEncontrado[0][5]

        if estado != "Activo":
            messagebox.showinfo("Info", "El credito ya esta finalizado")
            return

        if cuotasPagadas >= cuotasTotales:
            estado = "Finalizado"
            data.actualizarCredito(idCredito, cuotasPagadas, estado)
            messagebox.showinfo("Info", "El credito ya estaba finalizado")
            self.buscarCredito()
            return

        cuotasPagadas = cuotasPagadas + 1

        if cuotasPagadas >= cuotasTotales:
            estado = "Finalizado"

        actualizado = data.actualizarCredito(idCredito, cuotasPagadas, estado)

        if actualizado:
            messagebox.showinfo("Info", "Pago aplicado correctamente")
            self.buscarCredito()
        else:
            messagebox.showinfo("Info", "No se pudo aplicar el pago")

    def verDeuda(self):
        idCredito = self.GUI.entradaIdCredito.get()

        creditoEncontrado = data.buscarCreditoId(idCredito)

        if len(creditoEncontrado) == 0:
            messagebox.showinfo("Info", "Credito no encontrado")
            return

        montoPrestado = float(creditoEncontrado[0][2])
        cuotasTotales = int(creditoEncontrado[0][3])
        cuotasPagadas = int(creditoEncontrado[0][4])

        cuota = montoPrestado / cuotasTotales
        deudaPendiente = montoPrestado - (cuotasPagadas * cuota)

        messagebox.showinfo("Estado de Deuda", f"Deuda pendiente: {deudaPendiente}")