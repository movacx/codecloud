import tkinter as tkGUI
from tkinter import messagebox
from View.reportesGUI import ReportesGUI
import data.baseCliente as dataCliente
import data.baseCuenta as dataCuenta
import data.baseCredito as dataCredito


class ReportesController():
    def __init__(self, root):
        self.ventana = root
        self.GUI = ReportesGUI(root, self)

    def reporteLiquidez(self):
        cuentas = dataCuenta.listarCuentas()

        totalLiquidez = 0

        for item in cuentas:
            if item:
                try:
                    saldo = float(item[3])
                    totalLiquidez = totalLiquidez + saldo
                except:
                    continue

        arreglo = []
        arreglo.append(["Liquidez Total (Suma Saldos)", totalLiquidez])

        self.GUI.limpiarTabla()
        self.GUI.actualizarTabla(arreglo)

    def reporteRiesgo(self):
        creditos = dataCredito.listarCreditos()

        totalEnLaCalle = 0
        clientesConCredito = {}

        for item in creditos:
            if item:
                estado = item[5]
                if estado == "Activo":
                    dni = item[1]
                    montoPrestado = float(item[2])

                    if dni in clientesConCredito:
                        clientesConCredito[dni] = clientesConCredito[dni] + montoPrestado
                    else:
                        clientesConCredito[dni] = montoPrestado

                    totalEnLaCalle = totalEnLaCalle + montoPrestado

        arreglo = []
        arreglo.append(["Total en la calle (Creditos Activos)", totalEnLaCalle])

        for dni in clientesConCredito:
            arreglo.append([f"DNI {dni}", clientesConCredito[dni]])

        self.GUI.limpiarTabla()
        self.GUI.actualizarTabla(arreglo)

    def reporteRanking(self):
        clientes = dataCliente.listarClientes()
        cuentas = dataCuenta.listarCuentas()

        saldoPorCliente = {}

        for item in cuentas:
            if item:
                dni = item[2]
                try:
                    saldo = int(item[3])
                except:
                    saldo = 0

                if dni in saldoPorCliente:
                    saldoPorCliente[dni] = saldoPorCliente[dni] + saldo
                else:
                    saldoPorCliente[dni] = saldo

        listaRanking = []
        for cliente in clientes:
            dni = cliente[0]
            nombre = cliente[1]
            apellido = cliente[2]

            patrimonio = 0
            if dni in saldoPorCliente:
                patrimonio = saldoPorCliente[dni]

            listaRanking.append([patrimonio, dni, nombre, apellido])

        listaRanking.sort(reverse=True)

        arreglo = []
        contador = 0

        for item in listaRanking:
            if contador < 5:
                patrimonio = item[0]
                dni = item[1]
                nombre = item[2]
                apellido = item[3]
                arreglo.append([f"{nombre} {apellido} ({dni})", patrimonio])
                contador = contador + 1

        self.GUI.limpiarTabla()
        self.GUI.actualizarTabla(arreglo)