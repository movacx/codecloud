class Credito:
    def __init__(self, id_credito, dni_cliente, monto_prestado, cuotas_totales, cuotas_pagadas, estado):
        self.id_credito = id_credito
        self.dni_cliente = dni_cliente
        self.monto_prestado = monto_prestado
        self.cuotas_totales = cuotas_totales
        self.cuotas_pagadas = cuotas_pagadas
        self.estado = estado
        
    def pagar_cuota(self, monto):
        self.monto_prestado -= monto
        
    def exportar(self):
        return ([self.id_credito, self.dni_cliente, self.monto_prestado, self.cuotas_totales, self.cuotas_pagadas, self.estado])