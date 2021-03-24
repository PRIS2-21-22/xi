from Helpers.enums import TConvexidad
from Models.punto import Punto

# Clase que representa una figura geométrica, formada por la unión de puntos.
class Poligono:
    # Contructor por defecto de la clase.
    def __init__(self):
        print("Nuevo Polígono (por defecto)")
        self.puntos = [Punto(), Punto(), Punto()]
        self.convexidad = TConvexidad.Indefinido
        self.area = 0
        self.centroide = Punto()

    # Constructor que permite añadir puntos. Calcula la convexidad, área y centro de masas del polígono.
    def __init__(self, puntos):
        print("Nuevo Polígono (puntos asignados)")
        self.puntos = puntos
        set_convexidad()
        set_area()
        set_centroide()

    # Obtiene los puntos definidos para el polígono.
    def get_puntos(self): 
        return self.puntos

    # Asigna nuevos puntos al polígono y recalcula los valores afectados.
    def set_puntos(self, puntos):
        print("Asignando nuevos puntos...")
        self.puntos = puntos
        set_convexidad()
        set_area()
        set_centroide()

    # Obtiene la convexidad del polígono. Si aún no está definida, la calcula.
    def get_convexidad(self): 
        return self.convexidad

    # Calcula y asigna si el polígono es cóncavo o convexo.
    def set_convexidad(self):
        print("Determinando si es cóncavo o convexo...")
        res = TConvexidad.Indefinido
        # ...
        self.convexidad = res

    # Obtiene el area del polígono. Si aún no está definida, la calcula.
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
        print("Centro de masas determinado: " + res)

    # Mueve el polígono en el espacio.
    def mover(self):
        print("Moviendo el polígono en el espacio...")
        # ...
        print("Polígono trasladado a la nueva posición: " + str_puntos(str_separador=", "))

    # Imprime los puntos del polígono.
    def str_puntos(self, str_inicio = "\n", str_separador = "\n"):
        res = str_inicio + str_separador

        for punto in self.puntos:
            res = res + punto + str_separador

        return res[:len(res)-len(str_separador)]

    # Devuelve la representación textual del polígono, es decir, sus datos.
    def __str__(self):
     return "DATOS DEL POLÍGONO\n" + \
            "- Convexidad " + self.convexidad + \
            "- Área       " + self.area + " (u^2)" + \
            "- Centroide  " + self.centroide + \
            "- Puntos"      + self.str_puntos("\n   ", "\n\t· ")