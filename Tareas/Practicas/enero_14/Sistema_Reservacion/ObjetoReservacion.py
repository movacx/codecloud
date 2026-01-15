# Archivo: modelos.py

class Cliente:

    num_reservaciones = 1 

    #Constructor
    def __init__(self, nombre_cliente, noches, costoPor_noche, tipo_habitacion, costo_total):
        self.nombre_cliente = nombre_cliente
        self.noches = noches
        self.costoPor_noche = costoPor_noche
        self.tipo_habitacion = tipo_habitacion
        self.costo_total = costo_total
        
        Cliente.num_reservaciones += 1
        self.numero_reservacion = Cliente.num_reservaciones
        
    #Seccion de getters    
    def getNombre(self):
        return self.nombre_cliente
    def getNoches(self):
        return self.noches
    def getCostoPorNoche(self):
        return self.costoPor_noche
    def getTipoHabitacion(self):
        return self.tipo_habitacion
    def getCostoTotal(self):
        return self.costo_total
    def getNumReservacion(self):
        return self.num_reservaciones
        
    def __str__(self):
        return f"""
    --------- Factura --------
    Tipo de Habitacion: {self.tipo_habitacion}
    Costo de habitacion: {self.costoPor_noche}
    
    Nick: {self.nombre_cliente}
    Noches: {self.noches}
    Numero Reservacion: {self.numero_reservacion}
    
    Costo total: {self.costo_total}
    -----------------------------"""
    
    def mostrarDatos(self):
        print(f"""
              --------- Factura --------
              Tipo de Habitacion: {self.tipo_habitacion}
              Costo de habitacion: {self.costoPor_noche}
              
              Nick: {self.nombre_cliente}
              Noches: {self.noches}
              Numero Reservacion: {self.numero_reservacion}
              
              Costo total: {self.costo_total}
              -----------------------------
              """)
    
    def calcularCosto(self):
        total = self.costoPor_noche * self.noches
        return total
    
