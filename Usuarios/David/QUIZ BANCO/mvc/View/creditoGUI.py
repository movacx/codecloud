import tkinter as tk
from tkinter import ttk
from tkinter import Menu


class CreditoGUI:
    def __init__(self, ventanaPadre, creditoController):
        self.ventanaHija = tk.Toplevel(ventanaPadre)
        self.ventanaHija.title("Mantenimiento de Creditos")
        self.ventanaHija.geometry("1000x550")

        self.manejoController = creditoController

        self.frameContenedor = tk.Frame(self.ventanaHija)
        self.frameContenedor.grid(row=0, column=0, padx=20, pady=20)

        self.labels()
        self.entry()
        self.button()
        self.table()
#=========================================[ FIN CONSTRUCTOR ]==============================================#

    def labels(self):
        tk.Label(self.frameContenedor, text="ID Credito:").grid(row=0, column=0, sticky="e", pady=5)
        tk.Label(self.frameContenedor, text="DNI Cliente:").grid(row=1, column=0, sticky="e", pady=5)
        tk.Label(self.frameContenedor, text="Monto Prestado:").grid(row=2, column=0, sticky="e", pady=5)
        tk.Label(self.frameContenedor, text="Cuotas Totales:").grid(row=3, column=0, sticky="e", pady=5)
        tk.Label(self.frameContenedor, text="Monto Pago:").grid(row=4, column=0, sticky="e", pady=5)

    def entry(self):
        self.entradaIdCredito = tk.Entry(self.frameContenedor)
        self.entradaIdCredito.grid(row=0, column=1, pady=5)

        self.entradaDniCliente = tk.Entry(self.frameContenedor)
        self.entradaDniCliente.grid(row=1, column=1, pady=5)

        self.entradaMontoPrestado = tk.Entry(self.frameContenedor)
        self.entradaMontoPrestado.grid(row=2, column=1, pady=5)

        self.entradaCuotasTotales = tk.Entry(self.frameContenedor)
        self.entradaCuotasTotales.grid(row=3, column=1, pady=5)

        self.entradaMontoPago = tk.Entry(self.frameContenedor)
        self.entradaMontoPago.grid(row=4, column=1, pady=5)

    def button(self):
        self.btnSolicitarCredito = tk.Button(self.frameContenedor, text="Solicitar Credito", command=lambda: self.manejoController.solicitarCredito())
        self.btnSolicitarCredito.grid(row=5, column=0, pady=15, ipadx=1)

        self.btnPagarCuota = tk.Button(self.frameContenedor, text="Pagar Cuota", command=lambda: self.manejoController.pagarCuota())
        self.btnPagarCuota.grid(row=6, column=0, pady=15, ipadx=1)

        self.btnVerDeuda = tk.Button(self.frameContenedor, text="Ver Deuda", command=lambda: self.manejoController.verDeuda())
        self.btnVerDeuda.grid(row=5, column=1, pady=15, ipadx=1)

        self.btnBuscarCredito = tk.Button(self.frameContenedor, text="Buscar Credito", command=lambda: self.manejoController.buscarCredito())
        self.btnBuscarCredito.grid(row=6, column=1, pady=15, ipadx=1)

        self.btnListarCreditos = tk.Button(self.frameContenedor, text="Listar Creditos", command=lambda: self.manejoController.listarCreditos())
        self.btnListarCreditos.grid(row=5, column=2, pady=15, ipadx=1)

        self.btnLimpiarTabla = tk.Button(self.frameContenedor, text="Limpiar", command=lambda: self.limpiarTabla())
        self.btnLimpiarTabla.grid(row=10, column=5)

    def table(self):
        self.columnas = ["ID", "DNI", "Monto", "CuotasTotales", "CuotasPagadas", "Estado"]
        self.tabla = ttk.Treeview(self.frameContenedor, columns=self.columnas, show="headings")

        for items in self.columnas:
            self.tabla.heading(items, text=items.capitalize())
            self.tabla.column(items, width=120)
            self.tabla.grid(row=7, column=4, columnspan=3, sticky='nwse')

    def actualizarTabla(self, arreglo):
     for item in arreglo:
      if len(item) >= 6:
       self.tabla.insert("", tk.END, values=(item[0], item[1], item[2], item[3], item[4], item[5]))
       print(item)

    def limpiarTabla(self):
        for items in self.tabla.get_children():
            self.tabla.delete(items)

        self.entradaIdCredito.delete(0, tk.END)
        self.entradaDniCliente.delete(0, tk.END)
        self.entradaMontoPrestado.delete(0, tk.END)
        self.entradaCuotasTotales.delete(0, tk.END)
        self.entradaMontoPago.delete(0, tk.END)