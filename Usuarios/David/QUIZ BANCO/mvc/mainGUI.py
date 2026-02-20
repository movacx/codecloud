import tkinter as tk
from Controller.clienteController import ClienteController
from Controller.creditoController import CreditoController
from Controller.cuentaAhorroController import CuentaAhorroController
from Controller.reportesController import ReportesController


def main():
	ventanaPadre = tk.Tk()
	ventanaPadre.title("Sistema --Safe Bank--")
	ventanaPadre.geometry("500x550")
	# Label
	tk.Label(ventanaPadre, text="--SAFE BANK--").pack(pady=20)
	# Buttons
	tk.Button(ventanaPadre, text="Clientes", command=lambda: ClienteController(ventanaPadre)).pack(pady=5)
	tk.Button(ventanaPadre, text="Cuentas de ahorro", command=lambda: CuentaAhorroController(ventanaPadre)).pack(pady=5)
	tk.Button(ventanaPadre, text="Creditos", command=lambda: CreditoController(ventanaPadre)).pack(pady=5)
	tk.Button(ventanaPadre, text="Reportes", command=lambda: ReportesController(ventanaPadre)).pack(pady=5)
	tk.Button(ventanaPadre, text="Salir", command=ventanaPadre.destroy).pack(pady=20)
	
	
	ventanaPadre.mainloop()
	
	
if __name__ == "__main__":
	main()