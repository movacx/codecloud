class SistemaNotificaciones:
    def __init__(self):
        self.historial = []


    def ejecutar_sistema(self):
        print("\n===== SISTEMA DE NOTIFICACIONES =====")
        print("1. Enviar Email")
        print("2. Enviar SMS")
        print("3. Enviar WhatsApp")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ") 

        if opcion == "4":
            print("Saliendo...")
            return

        mensaje = input("Ingrese el mensaje: ")

        if opcion == "1":
            resultado = f"Email enviado: {mensaje}"
            print(f"Resultado: {resultado}")
            self.historial.append(resultado)
        elif opcion == "2":
            resultado = f"SMS enviado: {mensaje}"
            print(f"Resultado: {resultado}")
            self.historial.append(resultado)
        elif opcion == "3":
            resultado = f"WhatsApp enviado: {mensaje}"
            print(f"Resultado: {resultado}")
            self.historial.append(resultado)
        else:
            print("Opción inválida, ponete vivo.")


def main():
    sistema = SistemaNotificaciones()

    while True:
        sistema.ejecutar_sistema()
        break 

if __name__ == "__main__":
    main()