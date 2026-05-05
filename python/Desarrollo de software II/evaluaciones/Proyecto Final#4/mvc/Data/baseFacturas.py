import os
import csv

dirData = os.path.dirname(os.path.abspath(__file__))
ARCHIVO = os.path.join(dirData, "csv", "facturas.csv")
#Leer facturas 
def leerFacturas():
    try:
        if not os.path.exists(ARCHIVO): return []
        datos = [ ]
        
        with open(ARCHIVO, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            
            for items in reader:
                if items: 
                    datos.append(items)
                    
        return datos
    
    except Exception as error:
        print(f"Error leer facturas: {error}")
        return [ ]
#-----------------------------------------------------------------------------------------------------------------------
#Guardar factura 
def guardarFactura(fila):
    try:
        fila.append("Completado")
        
        with open(ARCHIVO, "a", newline="", encoding="utf-8") as file:
            csv.writer(file).writerow(fila)
        return True
    
    except Exception as error:
        print(f"Error guardar factura: {error}")
        return False
#-----------------------------------------------------------------------------------------------------------------------
#Cambiar estado de la factura
def cambiarEstadoFactura(idFac, nuevoEstado):
    try:
        facturas = leerFacturas()
        
        for items in facturas:
            if items:
                if items[0] == str(idFac):
                    items[-1] = nuevoEstado
                    
        with open(ARCHIVO, "w", newline="", encoding="utf-8") as file:
            csv.writer(file).writerows(facturas)
        return True
    
    except Exception as error:
        print(f"Error estado factura: {error}")
        return False
    
    