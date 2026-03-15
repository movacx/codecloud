import tkinter as tkGUI
from tkinter import messagebox


def sumar():
	numeroUno = int(datoA.get())
	numeroDos = int(datoB.get())
	resultado = numeroUno + numeroDos
	messagebox.showinfo("--Data--",f"Resultado:  {resultado}")
	print(resultado)

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

def dividir():
	numeroUno = int(datoA.get())
	numeroDos = int(datoB.get())
	resultado = numeroUno / numeroDos
	messagebox.showinfo("--Data--",f"Resultado:  {resultado}")

def calcularFactorial():
	numero = int(datoA.get())
	resultado = 1
	
	for item in range(1, numero +1):
		resultado = resultado * item
		
	messagebox.showinfo("--Data--",f"Resultado:  {resultado}")
	

def calcularRaiz():
	numero = int(datoA.get())
	resultado = numero ** 0.5
	messagebox.showinfo("--Data--",f"Resultado:  {resultado}")

def elevarNumeroCuadrado():
	numero = int(datoA.get())
	resultado = numero ** 2
	messagebox.showinfo("--Data--",f"Resultado:  {resultado}")

ventanaGUI = tkGUI.Tk( )

ventanaGUI.title("Super Calcu")
ventanaGUI.geometry("400x600")


tkGUI.Label(ventanaGUI, text = "Super Calcu").grid(row=0, column =2, padx =5, pady= 5)


tkGUI.Label(ventanaGUI, text = "Dato 1: ").grid(row=1, column =0, padx =5, pady= 5)
datoA = tkGUI.Entry(ventanaGUI)
datoA.grid(row=1, column = 1, padx =5, pady= 5)


tkGUI.Label(ventanaGUI, text = "Dato 2: ").grid(row=2, column =0, padx =5, pady= 5)
datoB = tkGUI.Entry(ventanaGUI)
datoB.grid(row=2, column = 1, padx =1, pady= 1)



tkGUI.Label(ventanaGUI, text = "Resultado: ").grid(row=3, column =0, padx =5, pady= 5)
datoResultado = tkGUI.Entry(ventanaGUI)
datoResultado.grid(row=3, column = 1, padx =1, pady= 1)

tkGUI.Button(ventanaGUI, text = "Suma", command=sumar).grid(row=4, column=0)
tkGUI.Button(ventanaGUI, text = "Resta", command = restar).grid(row = 4, column = 1)
tkGUI.Button(ventanaGUI, text = "Multi", command = multiplicar).grid(row = 4, column = 2)
tkGUI.Button(ventanaGUI, text = "Div", command = dividir).grid(row = 4, column = 3)

tkGUI.Button(ventanaGUI, text = "Facto", command = calcularFactorial).grid(row = 5, column = 0)
tkGUI.Button(ventanaGUI, text = "Raiz", command = calcularRaiz).grid(row = 5, column = 1)
tkGUI.Button(ventanaGUI, text = "al cuadrado", command = elevarNumeroCuadrado).grid(row = 5, column = 2)
ventanaGUI.mainloop( )