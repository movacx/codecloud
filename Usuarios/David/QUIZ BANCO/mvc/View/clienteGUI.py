import tkinter as tk
from tkinter import ttk
from tkinter import Menu


class ClienteGUI:
    def __init__(self, ventanaPadre, clientesController):
        self.ventanaHija = tk.Toplevel(ventanaPadre)
        self.ventanaHija.title("Mantenimiento de Clientes")
        self.ventanaHija.geometry("1000x550")

        self.manejoController = clientesController

        self.frameContenedor = tk.Frame(self.ventanaHija)
        self.frameContenedor.grid(row=0, column=0, padx=20, pady=20)

        self.labels()
        self.entry()
        self.button()
        self.table()
#=========================================[ FIN CONSTRUCTOR ]==============================================#

    def labels(self):
        tk.Label(self.frameContenedor, text="DNI:").grid(row=0, column=0, sticky="e", pady=5)
        tk.Label(self.frameContenedor, text="Nombre:").grid(row=1, column=0, sticky="e", pady=5)
        tk.Label(self.frameContenedor, text="Apellido:").grid(row=2, column=0, sticky="e", pady=5)
        tk.Label(self.frameContenedor, text="Email:").grid(row=3, column=0, sticky="e", pady=5)

    def entry(self):
        self.entradaDniCliente = tk.Entry(self.frameContenedor)
        self.entradaDniCliente.grid(row=0, column=1, pady=5)

        self.entradaNombreCliente = tk.Entry(self.frameContenedor)
        self.entradaNombreCliente.grid(row=1, column=1, pady=5)

        self.entradaApellidoCliente = tk.Entry(self.frameContenedor)
        self.entradaApellidoCliente.grid(row=2, column=1, pady=5)

        self.entradaEmailCliente = tk.Entry(self.frameContenedor)
        self.entradaEmailCliente.grid(row=3, column=1, pady=5)

    def button(self):
        self.btnGuardarCliente = tk.Button(self.frameContenedor, text="Registrar Cliente", command=lambda: self.manejoController.guardarCliente())
        self.btnGuardarCliente.grid(row=4, column=0, pady=15, ipadx=1)

        self.btnBuscarCliente = tk.Button(self.frameContenedor, text="Buscar Cliente", command=lambda: self.manejoController.buscarCliente())
        self.btnBuscarCliente.grid(row=5, column=0, pady=15, ipadx=1)

        self.btnEliminarCliente = tk.Button(self.frameContenedor, text="Eliminar Cliente", command=lambda: self.manejoController.eliminarCliente())
        self.btnEliminarCliente.grid(row=5, column=1)

        self.btnListarClientes = tk.Button(self.frameContenedor, text="Listar Clientes", command=lambda: self.manejoController.listarClientes())
        self.btnListarClientes.grid(row=5, column=2)

        self.btnLimpiarTabla = tk.Button(self.frameContenedor, text="Limpiar", command=lambda: self.limpiarTabla())
        self.btnLimpiarTabla.grid(row=10, column=5)

    def table(self):
        self.columnas = ["DNI", "Nombre", "Apellido", "Email"]
        self.tabla = ttk.Treeview(self.frameContenedor, columns=self.columnas, show="headings")

        for items in self.columnas:
            self.tabla.heading(items, text=items.capitalize())
            self.tabla.column(items, width=150)
            self.tabla.grid(row=6, column=4, columnspan=3, sticky='nwse')

    def actualizarTabla(self, arreglo):
     for item in arreglo:
      if len(item) >= 4:
       self.tabla.insert("", tk.END, values=(item[0], item[1], item[2], item[3]))
       print(item)

    def limpiarTabla(self):
        for items in self.tabla.get_children():
            self.tabla.delete(items)

        self.entradaDniCliente.delete(0, tk.END)
        self.entradaNombreCliente.delete(0, tk.END)
        self.entradaApellidoCliente.delete(0, tk.END)
        self.entradaEmailCliente.delete(0, tk.END)