from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

print('Creacion Cuadrado'.center(40, '-'))
cuadrado = Cuadrado(lado=5, color='azul')
print(cuadrado)
cuadrado.alto = -15
print(f'Area: {cuadrado.calcular_area()}')
#print(Cuadrado.mro())

print('Creacion de rectanfulo'.center(40, '-'))
rectangulo = Rectangulo(ancho=2, alto=6, color='rosa')
print(f'Area: {rectangulo.calular_area()}')
print(rectangulo)