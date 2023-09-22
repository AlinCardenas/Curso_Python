from InputDevice import InputDevice
class Mouse(InputDevice):
    countMouses = 0
    def __init__(self, inputType, trademark):
        Mouse.countMouses += 1
        super().__init__(inputType, trademark)
        self._idMouse = Mouse.countMouses

    def __str__(self):
        return f'{super().__str__()} El id es: {self._idMouse}'

if __name__ == '__main__':
    mouse = Mouse('Entrada', 'Sonic', )
    print(mouse)