import tkinter as tk
from tkinter import ttk
from tkinter import Menu


class ReportesGUI:
    def __init__(self, ventanaPadre, reportesController):
        self.ventanaHija = tk.Toplevel(ventanaPadre)
        self.ventanaHija.title("Reportes - SAFE BANK")
        self.ventanaHija.geometry("1000x550")

        self.manejoController = reportesController

        self.frameContenedor = tk.Frame(self.ventanaHija)
        self.frameContenedor.grid(row=0, column=0, padx=20, pady=20)

        self.labels()
        self.button()
        self.table()
#=========================================[ FIN CONSTRUCTOR ]==============================================#

    def labels(self):
        tk.Label(self.frameContenedor, text="Reportes del Banco").grid(row=0, column=0, sticky="w", pady=5)

    def button(self):
        self.btnLiquidez = tk.Button(self.frameContenedor, text="Reporte Liquidez", command=lambda: self.manejoController.reporteLiquidez())
        self.btnLiquidez.grid(row=1, column=0, pady=15, ipadx=1)

        self.btnRiesgo = tk.Button(self.frameContenedor, text="Reporte Riesgo", command=lambda: self.manejoController.reporteRiesgo())
        self.btnRiesgo.grid(row=2, column=0, pady=15, ipadx=1)

        self.btnRanking = tk.Button(self.frameContenedor, text="Ranking Clientes Top 5", command=lambda: self.manejoController.reporteRanking())
        self.btnRanking.grid(row=3, column=0, pady=15, ipadx=1)

        self.btnLimpiarTabla = tk.Button(self.frameContenedor, text="Limpiar", command=lambda: self.limpiarTabla())
        self.btnLimpiarTabla.grid(row=10, column=5)

    def table(self):
        self.columnas = ["Dato", "Valor"]
        self.tabla = ttk.Treeview(self.frameContenedor, columns=self.columnas, show="headings")

        for items in self.columnas:
            self.tabla.heading(items, text=items.capitalize())
            self.tabla.column(items, width=300)
            self.tabla.grid(row=4, column=4, columnspan=3, sticky='nwse')

    def actualizarTabla(self, arreglo):
     for item in arreglo:
      if len(item) >= 2:
       self.tabla.insert("", tk.END, values=(item[0], item[1]))
       print(item)

    def limpiarTabla(self):
        for items in self.tabla.get_children():
            self.tabla.delete(items)