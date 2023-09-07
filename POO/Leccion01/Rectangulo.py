class Rectangulo:
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base
    def calcular_area(self):
        print(f'El area es: {self.base * self.altura}')

base = int(input('Ingresa base '))
altura = int(input('Ingresa altura '))
obtenerArea = Rectangulo(altura, base )
obtenerArea.calcular_area()

