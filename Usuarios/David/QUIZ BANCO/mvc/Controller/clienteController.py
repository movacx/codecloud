import tkinter as tkGUI
from tkinter import messagebox
from View.clienteGUI import ClienteGUI
import data.baseCliente as data
from Model.clienteModel import ClienteModel


class ClienteController():

    def __init__(self, root):
        self.ventana = root
        self.GUI = ClienteGUI(root, self)

    # Metodo guardarCliente
    def guardarCliente(self):
        dni = self.GUI.entradaDniCliente.get().strip()
        nombre = self.GUI.entradaNombreCliente.get().strip()
        apellido = self.GUI.entradaApellidoCliente.get().strip()
        email = self.GUI.entradaEmailCliente.get().strip()

        if dni == "":
            messagebox.showinfo("Info", "Debe ingresar el DNI")
            return

        if nombre == "":
            messagebox.showinfo("Info", "Debe ingresar el nombre")
            return

        if apellido == "":
            messagebox.showinfo("Info", "Debe ingresar el apellido")
            return

        if email == "":
            messagebox.showinfo("Info", "Debe ingresar el email")
            return

        nuevoRegistro = ClienteModel(dni, nombre, apellido, email)
        guardado = data.guardarCliente(nuevoRegistro)

        if guardado:
            messagebox.showinfo("Info", "Cliente registrado correctamente")
            self.listarClientes()
        else:
            messagebox.showinfo("Info", "No se pudo registrar (DNI repetido o error)")

    # Metodo listarClientes
    def listarClientes(self):
        arreglo = data.listarClientes()
        self.GUI.limpiarTabla()
        self.GUI.actualizarTabla(arreglo)

    # Metodo buscarCliente
    def buscarCliente(self):
        dni = self.GUI.entradaDniCliente.get().strip()

        if dni == "":
            messagebox.showinfo("Info", "Debe ingresar el DNI para buscar")
            return

        encontrado = data.buscarCliente(dni)

        if len(encontrado) == 0:
            messagebox.showinfo("Info", "No se encontró el cliente")
            self.GUI.limpiarTabla()
            return

        self.GUI.limpiarTabla()
        self.GUI.actualizarTabla(encontrado)

    # Metodo eliminarCliente
    def eliminarCliente(self):
        dniEliminar = self.GUI.entradaDniCliente.get().strip()

        if dniEliminar == "":
            messagebox.showinfo("Info", "Debe ingresar el DNI para eliminar")
            return

        eliminado = data.eliminarCliente(dniEliminar)

        if eliminado:
            messagebox.showinfo("Info", "Cliente eliminado correctamente")
            self.listarClientes()
        else:
            messagebox.showinfo("Info", "No se encontró el cliente")