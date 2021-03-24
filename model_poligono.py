from model_punto import Punto
from helper_enums import TConvexidad

# Clase que representa una figura geométrica, formada por la unión de puntos.
class Poligono:
    # Constructor que permite añadir puntos. Calcula la convexidad, área y centro de masas del polígono.
    def __init__(self, puntos):
        print("Nuevo Polígono (puntos asignados)")
        self.puntos = puntos
        self.set_convexidad()
        self.set_area()
        self.set_centroide()

    # Obtiene los puntos definidos para el polígono.
    def get_puntos(self):
        return self.puntos

    # Asigna nuevos puntos al polígono y recalcula los valores afectados.
    def set_puntos(self, puntos):
        print("Asignando nuevos puntos...")
        self.puntos = puntos
        self.set_convexidad()
        self.set_area()
        self.set_centroide()

    # Obtiene la convexidad del polígono. Si aún no está definida, la calcula.
    def get_convexidad(self):
        return self.convexidad

    # Calcula y asigna si el polígono es cóncavo o convexo.
    def set_convexidad(self):
        print("Determinando si es cóncavo o convexo...")
        res = TConvexidad.Indefinido
        # ...
        self.convexidad = res

    # Obtiene el área del polígono. Si aún no está definida, la calcula.
    def get_area(self):
        return self.area

    # Calcula y asigna el área total del polígono.
    def set_area(self):
        print("Determinando el área total...")
        res = 0
        # ...
        self.area = res

    # Obtiene el centro de masas del polígono. Si aún no está definido, lo calcula.
    def get_centroide(self):
        return self.centroide

    # Calcula y asigna el centro de masas del polígono.
    def set_centroide(self):
        print("Determinando el centro de masas...")
        res = Punto()
        # ...
        self.centroide = res

    # Imprime los puntos del polígono.
    def str_puntos(self, str_inicio = "\n", str_separador = "\n"):
        res = str_inicio + str_separador

        for punto in self.puntos:
            res = res + str(punto) + str_separador

        return res[:len(res)-len(str_separador)]

    # Mueve el polígono en el espacio.
    def mover(self):
        print("Moviendo el polígono en el espacio...")
        # ...

    # Devuelve la representación textual del polígono, es decir, sus datos.
    def __str__(self):
     return "\nDATOS DEL POLÍGONO" + \
            "\n- Convexidad => " + str(self.convexidad)[12:] + \
            "\n- Área       => " + str(self.area) + " (u^2)" + \
            "\n- Centroide  => " + str(self.centroide) + \
            "\n- Puntos "        + self.str_puntos("", "\n  · ") + \
            "\n"