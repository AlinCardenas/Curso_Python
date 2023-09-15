from Cuadrado import Cuadrado
from FiguraGeometrica import FiguraGeometrica
from Rectangulo import Rectangulo

#no se puede instanciar una clase abstracta figura = FiguraGeometrica()
print('Creacion Cuadrado'.center(40, '-'))
cuadrado = Cuadrado(lado=5, color='azul')
print(cuadrado)
cuadrado.alto = -15
print(f'Area: {cuadrado.calcular_area()}')
#print(Cuadrado.mro())

print('Creacion de rectangulo'.center(40, '-'))
rectangulo = Rectangulo(ancho=2, alto=6, color='rosa')
print(f'Area: {rectangulo.calcular_area()}')
print(rectangulo)