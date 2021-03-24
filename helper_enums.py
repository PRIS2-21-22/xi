import enum

# Clase que contiene los tipos de convexidad y un estado de "no calculado".
class TConvexidad(enum.Enum):
    Indefinido = 0
    Concavo = 1
    Convexo = 2