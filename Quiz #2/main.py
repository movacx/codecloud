# === SISTEMA DE CONDOMINIOS COSTAMAR ===
# 1. Gestionar Habitaciones
# 2. Gestionar Huéspedes
# 3. Gestionar Reservas
# 4. Reportes
# 5. Salir
from controller.habitacionesController import HabitacionController


def main():

    hCtrl = HabitacionController()


    while True:
        print("""
            === SISTEMA DE CONDOMINIOS COSTAMAR ===
            1. Gestión de Habitaciones
            2. Gestión de Huéspedes
            3. Gestión de Reservas
            4. Reportes
            5. Salir
            """)

        op = input("Seleccione: ")
        if op == "1":
            pass

        elif op == "2":
            pass

        elif op == "3":
            pass

        elif op == "4":
            pass

        elif op == "5":
            break



   

if __name__ == "__main__":
    main()
