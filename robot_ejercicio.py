class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0
    def adelante(self):
        self.x +=1
        return "("+str(self.x)+","+str(self.y)+")"
    def retroceder(self):
        self.x-=1
        return "("+str(self.x)+","+str(self.y)+")"
    def mover_derecha(self):
        self.y +=1
        return "("+str(self.x)+","+str(self.y)+")"
    def mover_izquierda(self):
        self.y -=1
        return "("+str(self.x)+","+str(self.y)+")"

Robotito = Robot()
print(Robotito.adelante())
print(Robotito.adelante())
print(Robotito.mover_izquierda())
print(Robotito.adelante())
print(Robotito.mover_derecha())
print(Robotito.mover_derecha())
print(Robotito.mover_derecha())
print(Robotito.retroceder())
print(Robotito.mover_izquierda())
x