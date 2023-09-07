class  Aritmetica:
    """
    clase para realizar operaciones
    """
    def __init__(self, firstNumber, secondNumber):
        self.firstNumber = firstNumber
        self.secondNumber = secondNumber

    def suma(self):
        print(f'La suma es: {self.firstNumber+self.secondNumber}')
    def resta(self):
        print(f'La resta es: {self.firstNumber-self.secondNumber}')
    def multiplicacion(self):
        print(f'La multiplicacion es: {self.firstNumber * self.secondNumber}')
    def division(self):
        print(f'La division es: {self.firstNumber / self.secondNumber}')

operaciones = Aritmetica(8,9)
operaciones.suma()
operaciones.resta()
operaciones.multiplicacion()
operaciones.division()
