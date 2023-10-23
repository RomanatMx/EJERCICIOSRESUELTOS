"""
Ejercicio 3
Mejora el ejercicio anterior de forma que el robot pueda recibir una secuencia de movimientos.
Ejemplo:
• mueve(“AADDADIR”) # (2,2)
También deberá tener otros dos métodos: uno que devuelva todas las órdenes recibidas y otro capaz
de listar los movimientos necesarios para volver a la posición inicial (0,0).

"""
class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.movimientos = ""
    def mueve(self, movimiento: str):
        self.movimientos = movimiento
        for i in movimiento:
            if i == "A":
                self.x += 1
            elif i == "R":
                self.x-=1
            elif i == "I":
                self.y -=1
            elif i == "D":
                self.y +=1
            else:
                return "Caracter incorrecto" 
                break
        return "("+str(self.x)+","+str(self.y)+")"
    def devolver_ordenes_recibidas(self):
        return self.movimientos
    def posicion_inicial(self):
        self.x = 0
        self.y = 0
        return "("+str(self.x)+","+str(self.y)+")"

Robotito = Robot()
print(Robotito.mueve("AADDADIR")) # Resultado -> (2,2)
print(Robotito.devolver_ordenes_recibidas()) # Resultado -> "AADDADIR"
print(Robotito.posicion_inicial()) # Resultado -> (0,0)
