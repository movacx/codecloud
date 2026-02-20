import tkinter as tk
from tkinter import ttk
from tkinter import Menu


class CuentaAhorroGUI:
    def __init__(self, ventanaPadre, cuentaAhorroController):
        self.ventanaHija = tk.Toplevel(ventanaPadre)
        self.ventanaHija.title("Mantenimiento de Cuentas de Ahorro")
        self.ventanaHija.geometry("1000x550")

        self.manejoController = cuentaAhorroController

        self.frameContenedor = tk.Frame(self.ventanaHija)
        self.frameContenedor.grid(row=0, column=0, padx=20, pady=20)

        self.labels()
        self.entry()
        self.button()
        self.table()
#=========================================[ FIN CONSTRUCTOR ]==============================================#

    def labels(self):
        tk.Label(self.frameContenedor, text="Numero de Cuenta:").grid(row=0, column=0, sticky="e", pady=5)
        tk.Label(self.frameContenedor, text="DNI Cliente:").grid(row=1, column=0, sticky="e", pady=5)
        tk.Label(self.frameContenedor, text="Saldo:").grid(row=2, column=0, sticky="e", pady=5)
        tk.Label(self.frameContenedor, text="Interes Anual:").grid(row=3, column=0, sticky="e", pady=5)
        tk.Label(self.frameContenedor, text="Monto:").grid(row=4, column=0, sticky="e", pady=5)

    def entry(self):
        self.entradaNumeroCuenta = tk.Entry(self.frameContenedor)
        self.entradaNumeroCuenta.grid(row=0, column=1, pady=5)

        self.entradaDniCliente = tk.Entry(self.frameContenedor)
        self.entradaDniCliente.grid(row=1, column=1, pady=5)

        self.entradaSaldo = tk.Entry(self.frameContenedor)
        self.entradaSaldo.grid(row=2, column=1, pady=5)

        self.entradaInteresAnual = tk.Entry(self.frameContenedor)
        self.entradaInteresAnual.grid(row=3, column=1, pady=5)

        self.entradaMonto = tk.Entry(self.frameContenedor)
        self.entradaMonto.grid(row=4, column=1, pady=5)

    def button(self):
        self.btnAperturaCuenta = tk.Button(
            self.frameContenedor,
            text="Apertura Cuenta",
            command=lambda: self.manejoController.abrirCuentaAhorro()
        )
        self.btnAperturaCuenta.grid(row=5, column=0, pady=15, ipadx=1)

        self.btnDeposito = tk.Button(
            self.frameContenedor,
            text="Deposito",
            command=lambda: self.manejoController.depositar()
        )
        self.btnDeposito.grid(row=6, column=0, pady=15, ipadx=1)

        self.btnRetiro = tk.Button(
            self.frameContenedor,
            text="Retiro",
            command=lambda: self.manejoController.retirar()
        )
        self.btnRetiro.grid(row=5, column=1, pady=15, ipadx=1)

        self.btnAplicarInteres = tk.Button(
            self.frameContenedor,
            text="Aplicar Interes",
            command=lambda: self.manejoController.aplicarInteres()
        )
        self.btnAplicarInteres.grid(row=6, column=1, pady=15, ipadx=1)

        self.btnBuscarCuenta = tk.Button(
            self.frameContenedor,
            text="Buscar Cuenta",
            command=lambda: self.manejoController.buscarCuenta()
        )
        self.btnBuscarCuenta.grid(row=5, column=2, pady=15, ipadx=1)

        self.btnListarCuentas = tk.Button(
            self.frameContenedor,
            text="Listar Cuentas",
            command=lambda: self.manejoController.listarCuentas()
        )
        self.btnListarCuentas.grid(row=6, column=2, pady=15, ipadx=1)

        self.btnLimpiarTabla = tk.Button(
            self.frameContenedor,
            text="Limpiar",
            command=lambda: self.limpiarTabla()
        )
        self.btnLimpiarTabla.grid(row=10, column=5)

    def table(self):
        self.columnas = ["Tipo", "NumeroCuenta", "DNI", "Saldo", "Interes"]
        self.tabla = ttk.Treeview(self.frameContenedor, columns=self.columnas, show="headings")

        for items in self.columnas:
            self.tabla.heading(items, text=items.capitalize())
            self.tabla.column(items, width=120)

        self.tabla.grid(row=7, column=4, columnspan=3, sticky='nwse')

    def actualizarTabla(self, arreglo):
        for item in arreglo:
            if len(item) >= 5:
                self.tabla.insert("", tk.END, values=(item[0], item[1], item[2], item[3], item[4]))
                print(item)

    def limpiarTabla(self):
        for items in self.tabla.get_children():
            self.tabla.delete(items)

        self.entradaNumeroCuenta.delete(0, tk.END)
        self.entradaDniCliente.delete(0, tk.END)
        self.entradaSaldo.delete(0, tk.END)
        self.entradaInteresAnual.delete(0, tk.END)
        self.entradaMonto.delete(0, tk.END)