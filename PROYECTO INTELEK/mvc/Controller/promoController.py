import random

class PromoController:
    def aplicarSuerte(self, totalPlata):
        suerte = random.randint(1, 100) 
        montoFinal = float(totalPlata)
        if suerte <= 10:
            return montoFinal * 0.20, "Felicidades! 80% de descuento"
        return montoFinal * 0.75, "Ganaste 25% de descuento"