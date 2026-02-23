import tkinter as tkGUI
from tkinter import messagebox
from View.habitacionGUI import HabitacionGUI
import Data.baseHabitacion as data
from Model.habitacionModel import HabitacionModel


class HabitacionController():
    def __init__(self, root):
        self.ventana = root
        self.GUI = HabitacionGUI(root, self)
        
    def obtenerUltimoId(self):
        ultimoId = data.validarUltimoId()
        return ultimoId
    
    def guardarHabitacion(self):
        numero = self.GUI.entradaNumeroHabitacion.get()
        tipo = self.GUI.comboboxTipoHabitacion.get()
        precio = self.GUI.entradaPrecioHabitacion.get()
        estado = self.GUI.comboboxEstadoHabitacion.get()
        nuevoRegistro = HabitacionModel(0, numero, tipo, precio, estado)
        data.registrarHabitacion(nuevoRegistro)
        
    def ordenarHabitacionPrecio(self):
        arreglo = data.ordenarPrecio()
        print("Ordenado:", arreglo)
        self.GUI.limpiarTabla()
        self.GUI.actualizarTabla(arreglo)
		
    def listarHabitacion(self):
        arreglo = data.listarHabitaciones()
        self.GUI.limpiarTabla()
        self.GUI.actualizarTabla(arreglo)
        
        
    def buscarHabitacion(self):
        numero = self.GUI.entradaNumeroHabitacion.get()
        encontrado = data.buscarHabitacionId(numero)
        self.GUI.limpiarTabla()
        self.GUI.actualizarTabla(encontrado)
        
        
    def modificarEstadoHabitacion(self):
        seleccion = self.GUI.entradaNumeroHabitacion.get()
        estado = self.GUI.comboboxEstadoHabitacion.get()
        data.modificar(seleccion, estado)
        self.listarHabitacion()
            
    def eliminarHabitacion(self):
        numeroEliminar = self.GUI.entradaNumeroHabitacion.get()
        habitacionEliminar = data.eliminarHabitacion(numeroEliminar)
        messagebox.showinfo("Info", "Modificado correctamente")
        
    def botonClick(self, boton):
        if boton == "x":
            print ("El usuario dio click")
            messagebox.showinfo("Prueba", "El usuario clickeo un boton")
