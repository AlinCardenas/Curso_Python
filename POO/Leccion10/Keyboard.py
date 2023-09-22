from InputDevice import *
class Keyboard(InputDevice):
    countKeyboard = 0
    def __init__(self, inputType, trademark):
        Keyboard.countKeyboard += 1
        super().__init__(inputType, trademark)
        self.idKeyboard = Keyboard.countKeyboard

    def __str__(self):
        return f'{super().__str__()} El id es: {self.idKeyboard}'

if __name__ == '__main__':
    teclado = Keyboard('Entrada', 'samsung')
    print(teclado)