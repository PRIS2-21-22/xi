import helper_constantes as const
from model_punto import Punto
from model_vector import Vector
from model_poligono import Poligono

print("\n" + const.SEPARADOR)
print("| POLINOXI > TESTS                                                               |")
print(const.SEPARADOR)

print("\nTESTS DE 'PUNTO'")
print(Punto())

print("\nTESTS DE 'VECTOR'")
print(Vector())

print("\nTESTS DE 'POLINOMIO'")
print(Poligono([Punto(1, 2), Punto(1, 3), Punto(2, 3)]))