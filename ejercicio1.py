import math
class Triangulo:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura

    def area(self):
        area=self.base*self.altura/2
        print ("Area del triangulo: ",area)
    def perimetro(self):
        lado1=float(input("Ingrese el lado 1 del triangulo: "))
        lado2=float(input("Ingrese el lado 2 del triangulo: "))
        perimetro=lado1+lado2+self.base
        print("Perimetro del triangulo: ", perimetro)

class Rectangulo(Triangulo):
    def area(self):
        area=self.base*self.altura
        print("Area del rectangulo: ",area)
    def perimetro(self):
       perimetro=2*self.base+2*self.altura
       print("Perimetro del rectangulo:", perimetro)
    
class Circulo:
    def __init__(self,radio):
        self.radio=radio
    def area(self):
        area=math.pi*(self.radio)**2
        print("Area del circulo:",area)
    def perimetro(self):
        perimetro=2*math.pi*self.radio
        print("Perimetro del circulo:", perimetro)

triangulo1=Triangulo(12,6)
rectangulo1=Rectangulo(32,12)
circulo1=Circulo(23)
figuras=[triangulo1,rectangulo1,circulo1]

for i in figuras:
    i.area()
    i.perimetro()


