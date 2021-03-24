from model_punto import Punto

# Clase que permite relacionar dos puntos geométricamente.
class Vector:
    # Contructor que permite asignar coordenadas para los dos puntos del vector.
    def __init__(self, x1 = 0, y1 = 0, x2 = 0, y2 = 0):
        print("Nuevo Vector (X1, Y1, X2 e Y2 asignados)")
        self.p1 = Punto(x1, y1)
        self.p2 = Punto(x2, y2)

    # Devuelve la representación textual del vector, es decir, sus coordenadas.
    def __str__(self):
        return "[ P1:" + str(self.p1) + ", P2:" + str(self.p2) + " ]"