import csv
from Model.reservaModel import Reserva

ARCHIVO = "Data/csv/reservas.csv"

def guardar_reservas(lista_reservas):
    with open(ARCHIVO, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        for rows in lista_reservas:
            writer.writerow([rows.id_reserva,rows.numero_habitacion,rows.id_huesped,rows.fecha_entrada,rows.fecha_salida])

def cargar_reservas():
    reservas = []
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    reservas.append(
                        Reserva(row[1],row[2],row[3],row[4],row[0])
                    )
    except FileNotFoundError:
        pass
    return reservas
