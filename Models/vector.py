from Models.punto import Punto

# Clase que permite relacionar dos puntos geométricamente.
class Vector:
    # Contructor por defecto de la clase.
    def __init__(self):
        print("Nuevo Vector (por defecto)")
        self.x = 0
        self.y = 0
        
    # Contructor que permite asignar los dos puntos que forman el vector.
    def __init__(self, p1, p2):
        print("Nuevo Vector (P1 y P2 asignados)")
        self.p1 = p1
        self.p2 = p2
        
    # Contructor que permite asignar coordenadas para los dos puntos del vector.
    def __init__(self, x1, y1, x2, y2):
        print("Nuevo Vector (X1, Y1, X2 e Y2 asignados)")
        self.p1 = Punto(x1, y1)
        self.p2 = Punto(x2, y2)

    # Devuelve la representación textual del vector, es decir, sus coordenadas.
    def __str__(self):
        return "[ P1:" + self.p1 + ", P2:" + p2 + " ]"