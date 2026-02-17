class Credito:
    def __init__(self, idCredito, dniCliente, montoPrestado, cuotasTotales):
        self.idCredito=idCredito
        self.dniCliente=dniCliente
        self.montoPrestado=montoPrestado
        self.cuotasTotales=cuotasTotales
        self.estado = "Activo"
        
        def pagarCuota(self, monto):
            if self.estado == "Finalizado":
                print("Este credito se ha cancelado")
                return
            
            
                if self.cuotasPagadas == self.cuotasTotales:
                    self.estado = "Finalizado"
                
                    print("Credito finalizado")
            else:
                self.estado="Finalizado"
                
         def importarCsv(self):
            return [(self.idCredito, self.dniCliente, self.montoPrestado, self.cuotasTotales)]
                    
            