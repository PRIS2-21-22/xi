# Clase que permite definir una ubicación cualquiera en el espacio.
class Punto:
    # Contructor que permite asignar coordenadas al punto en ambos ejes (X e Y).
    def __init__(self, x = 0, y = 0):
        print("Nuevo Punto (X e Y asignados)")
        self.x = x
        self.y = y

    # Devuelve la representación textual del punto, es decir, sus coordenadas.
    def __str__(self):
        return "(X: " + str(self.x) + ", Y: " + str(self.y) + ")"