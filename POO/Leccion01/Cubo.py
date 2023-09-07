class Cubo:
    def __init__(self, alto, ancho, profundidad):
        self.alto = alto
        self.ancho = ancho
        self.profundidad = profundidad
    def calcular_volumen(self):
        return self.ancho*self.profundidad*self.alto
alto = int(input('Ingresa alto'))
ancho = int(input('Ingresa ancho'))
profundidad = int(input('Ingresa ancho'))
obtenerVolumen = Cubo(alto, ancho, profundidad)
print(f'{obtenerVolumen.calcular_volumen()} m3')
