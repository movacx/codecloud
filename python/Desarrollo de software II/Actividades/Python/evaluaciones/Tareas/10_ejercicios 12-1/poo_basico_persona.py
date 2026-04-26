class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def presentarse(self):
        print(f"Hola me llamo {self.nombre} y tengo {self.edad} años")
        
persona1 = Persona('Herlin',22)
persona2 = Persona('Laura', 100)

persona1.presentarse()
persona2.presentarse()

#se implemento "poo basic" sinceramente aun no lo domino del todo pero esta mas simple que en java