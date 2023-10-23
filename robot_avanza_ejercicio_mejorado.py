class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0
    def mueve(self, movimiento: str):
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
    def posicion_inicial(self):
        self.x = 0
        self.y = 0
        return "("+str(self.x)+","+str(self.y)+")"

Robotito = Robot()
print(Robotito.mueve("AADDADIR"))
print(Robotito.posicion_inicial())
