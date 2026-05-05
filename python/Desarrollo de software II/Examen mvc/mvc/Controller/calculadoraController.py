import tkinter as tk
from tkinter import messagebox
from Model.calculadoraModel import Model
from View.calculadoraView import calculadoraView
from View.historialView import HistorialView 
from Data.calculadoraData import Data


class Controller:
    
    def __init__(self, root):
        self.root = root
        self.modelo = Model()
        self.GUI = calculadoraView(root, self)
        self.manejoData = Data()

    def calcular(self):
        numeroUno = self.GUI.numeroUno.get()
        numeroDos = self.GUI.numeroDos.get()
        operacion = self.GUI.operacion.get()


        if not (numeroUno or numeroDos or operacion):
            self.GUI.mostrarAdvertencia('Debe de completar todos los campos')
            return

        try:
            num1 = float(numeroUno)
            num2 = float(numeroDos)
        except ValueError:
            self.GUI.mostrarAdvertencia('Debe de ingresar numeros')

        if operacion == '+':
            resultado = self.modelo.sumar(num1, num2)
        elif operacion == '-':
            resultado = self.modelo.restar(num1, num2)
        elif operacion == '*':
            resultado = self.modelo.multiplicar(num1, num2)
        elif operacion == '/':
            resultado = self.modelo.dividir(num1, num2)

        self.modelo.setOperacion(operacion)
        self.GUI.actualizarResultado(resultado)

        self.manejoData.registrarHistorial(self.modelo)

    def abrirHistorial(self):
 
        historialGUI = HistorialView(self.root, self)
        

        arregloDatos = self.manejoData.mostrarHistorial()
        
        if arregloDatos:
            for items in arregloDatos:
                if items:

                    historialGUI.tabla.insert('', tk.END, values=(items[0], items[1], items[2], items[3], items[4]))