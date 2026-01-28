def reporte_reservas_activas(reservas):
    print(" Reservaciones activas")
    for rows in reservas:
        print(rows.mostrar_info())