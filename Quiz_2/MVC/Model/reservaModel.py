class Reserva:    
    def __init__(self, numero_habitacion, id_huesped, fecha_entrada, fecha_salida):

        self.numero_habitacion = numero_habitacion
        self.id_huesped, = id_huesped,    
        self.id = Estudiante.contadorIdEstudiante
        self.fecha_entrada, = fecha_entrada   
        self.fecha_salida, = fecha_salida    
             
#get
    def getNumero_Habitacion(self):
         return self numero_habitacion
    
    def getId_Huesped(self):
         return self.id_huesped

    def getFecha_Entrada(self):
         return self.fecha_entrada        
    
    def getFecha_Salida(self): 
        return self.fecha_salida
   
#set

     def setNumero_Habitacion(self,numero_Habitacion)
     return self.numero_habitacion
    
    def setId_Huesped(self, id_huesped):
         return self.id_huesped

    def setFecha_Entrada(self, fecha_Entrada):
         return self.fecha_entrada        

    
    def setFecha_Salida(self, fecha_Salida):
         return self.fecha_salida 

#Metodo poliformismo
#   
    def mostrandoDatos(self):
        return f"ID : {self.id_huesped}, {self.numero_habitacion}, {self.fecha_entrada}, {self.fecha_salida}"