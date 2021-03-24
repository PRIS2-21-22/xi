# Clase que permite definir una ubicación cualquiera en el espacio.
class Punto:
    # Contructor por defecto de la clase.
    def __init__(self):
        print("Nuevo Punto (por defecto)")
        self.x = 0
        self.y = 0
        
    # Contructor que permite asignar coordenadas al punto en ambos ejes (X e Y).
    def __init__(self, x, y):
        print("Nuevo Punto (X e Y asignados)")
        self.x = x
        self.y = y

    # Devuelve la representación textual del punto, es decir, sus coordenadas.
    def __str__(self):
        return "(X: " + self.x + ", Y: " + self.y + ")"