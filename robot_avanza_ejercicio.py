"""
Crea una clase Robot que simule los movimientos de un robot y calcule la posición en la que se
encuentra cada momento. El robot se moverá por un tablero infinito de coordenadas X e Y, podrá
realizar los siguientes movimientos:
• Avanzar hacia adelante (A)
• Retroceder (R)
• Avanzar hacia la izquierda (I) o hacia la derecha (D)
El robot tendrá un método llamado mueve() que recibirá la orden como parámetro y otro método,
posicion_actual(), que indicará su posición en las coordenadas X e Y. Al crear el robot este se
inicializará a las coordenadas (0,0).
Ejemplo:
• mueve(“A”) # (1,0)
• mueve(“A”) # (2,0)
• mueve(“I”) # (2,-1)
• mueve(“A”) # (3,-1)
• mueve(“D”) # (3,0)
• mueve(“D”) # (3,1)
• mueve(“D”) # (3,2)
• mueve(“R”) # (2,2)
• mueve(“I”) # (2,1)
"""
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
