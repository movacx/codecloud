import  os
import sys
import csv

sys.stdout.reconfigure(enconding = "utf-8")

import csv

BASE_DIR = os.path.dirname(os.path.abspath((__file__)))

ARCHIVO = os.path.join(BASE_DIR, 'csv', 'baseReserva.csv')