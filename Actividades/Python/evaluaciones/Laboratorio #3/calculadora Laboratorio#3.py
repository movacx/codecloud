import tkinter as tkGUI
from tkinter import messagebox

#---------------------------------------------------------------------

def sumar():
	numeroUno = int(datoA.get())
	numeroDos = int(datoB.get())
	resultado = numeroUno + numeroDos
	messagebox.showinfo("--Data--",f"Resultado:  {resultado}")
	print(resultado)
#---------------------------------------------------------------------

def restar():
	numeroUno = int(datoA.get())
	numeroDos = int(datoB.get())
	resultado = numeroUno - numeroDos
	messagebox.showinfo("--Data--",f"Resultado:  {resultado}")

def multiplicar():
	numeroUno = int(datoA.get())
	numeroDos = int(datoB.get())
	resultado = numeroUno * numeroDos
	messagebox.showinfo("--Data--",f"Resultado:  {resultado}")
#---------------------------------------------------------------------

def dividir():
	numeroUno = int(datoA.get())
	numeroDos = int(datoB.get())
	resultado = numeroUno / numeroDos
	messagebox.showinfo("--Data--",f"Resultado:  {resultado}")
#---------------------------------------------------------------------	

def calcularFactorial():
	numero = int(datoA.get())
	resultado = 1
	
	for item in range(1, numero +1):
		resultado = resultado * item
		
	messagebox.showinfo("--Data--",f"Resultado:  {resultado}")
	
#---------------------------------------------------------------------

def calcularRaiz():
	numero = int(datoA.get())
	resultado = numero ** 0.5
	messagebox.showinfo("--Data--",f"Resultado:  {resultado}")
#---------------------------------------------------------------------

def elevarNumeroCuadrado():
	numero = int(datoA.get())
	resultado = numero ** 2
	messagebox.showinfo("--Data--",f"Resultado:  {resultado}")
#---------------------------------------------------------------------
#GENERAR VENTANA 
ventanaGUI = tkGUI.Tk( )

ventanaGUI.title("--CALCULADORA--")
ventanaGUI.geometry("400x300")


tkGUI.Label(ventanaGUI, text = "--CALCULADORA--").grid(row=0, column =2, padx =5, pady= 5)

#-----------------------------------------------------------------------------
#label input
tkGUI.Label(ventanaGUI, text = "Dato 1: ").grid(row=1, column =0, padx =5, pady= 5)
datoA = tkGUI.Entry(ventanaGUI)
datoA.grid(row=1, column = 1, padx =5, pady= 5)

#-----------------------------------------------------------------------------
#label input
tkGUI.Label(ventanaGUI, text = "Dato 2: ").grid(row=2, column =0, padx =5, pady= 5)
datoB = tkGUI.Entry(ventanaGUI)
datoB.grid(row=2, column = 1, padx =1, pady= 1)


#-----------------------------------------------------------------------------
#label resultado
tkGUI.Label(ventanaGUI, text = "Resultado: ").grid(row=3, column =0, padx =5, pady= 5)
datoResultado = tkGUI.Entry(ventanaGUI)
datoResultado.grid(row=3, column = 1, padx =1, pady= 1)
#-----------------------------------------------------------------------------
#+
tkGUI.Button(ventanaGUI, text="Sumar", command=sumar).grid(row=1, column=2)
tkGUI.Button(ventanaGUI, text = "Restar", command = restar).grid(row = 1, column = 2)
tkGUI.Button(ventanaGUI, text = "Multiplicar", command = multiplicar).grid(row = 4, column = 2)
tkGUI.Button(ventanaGUI, text = "Dividir", command = dividir).grid(row = 2, column = 3)
#-----------------------------------------------------------------------------
#Raiz ! potencia
tkGUI.Button(ventanaGUI, text = "Factorial", command = calcularFactorial).grid(row = 4, column = 0)
tkGUI.Button(ventanaGUI, text = "Raiz", command = calcularRaiz).grid(row = 2, column = 2)
tkGUI.Button(ventanaGUI, text = "Elevar al cuadrado", command = elevarNumeroCuadrado).grid(row = 3, column = 2)

ventanaGUI.mainloop( )