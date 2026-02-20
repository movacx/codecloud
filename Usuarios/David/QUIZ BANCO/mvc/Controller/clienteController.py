import tkinter as tkGUI
from tkinter import messagebox
from View.clienteGUI import ClienteGUI
import data.baseCliente as data
from Model.clienteModel import ClienteModel


class ClienteController():
	
    def __init__(self, root):
        self.ventana = root
        self.GUI = ClienteGUI(root, self)
        
    #Metodo guardarCliente
    def guardarCliente(self):
        dni = self.GUI.entradaDniCliente.get()
        nombre = self.GUI.entradaNombreCliente.get()
        apellido = self.GUI.entradaApellidoCliente.get()
        email = self.GUI.entradaEmailCliente.get()

        nuevoRegistro = ClienteModel(dni, nombre, apellido, email)
        guardado = data.guardarCliente(nuevoRegistro)

        if guardado:
            messagebox.showinfo("Info", "Cliente registrado correctamente")
            self.listarClientes()
        else:
            messagebox.showinfo("Info", "No se pudo registrar (DNI repetido o error)")
            
     #Metodo listarClientes
    def listarClientes(self):
        arreglo = data.listarClientes()
        self.GUI.limpiarTabla()
        self.GUI.actualizarTabla(arreglo)
        
     #Metodo buscarCliente
    def buscarCliente(self):
        dni = self.GUI.entradaDniCliente.get()
        encontrado = data.buscarCliente(dni)
        self.GUI.limpiarTabla()
        self.GUI.actualizarTabla(encontrado)
        
     #Metodo eliminarCliente
    def eliminarCliente(self):
        dniEliminar = self.GUI.entradaDniCliente.get()
        eliminado = data.eliminarCliente(dniEliminar)

        if eliminado:
            messagebox.showinfo("Info", "Cliente eliminado correctamente")
            self.listarClientes()
        else:
            messagebox.showinfo("Info", "No se encontró el cliente")
            
            
            
            
