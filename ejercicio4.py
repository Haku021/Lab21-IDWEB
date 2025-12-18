from ejercicio1 import Triangulo, Rectangulo, Circulo

triangulo1 = Triangulo(12, 6)
rectangulo1 = Rectangulo(32, 12)
circulo1 = Circulo(23)

figuras = [triangulo1, rectangulo1, circulo1]

for i in figuras:
    i.area()
    i.perimetro()
    print()
    