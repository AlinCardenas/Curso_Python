class InputDevice:
    def __init__(self, inputType, trademark):
        self._inputType = inputType
        self._trademark = trademark

    @property
    def inputType(self):
        return self._inputType
    @inputType.setter
    def inputType(self, inputType):
        self._inputType = inputType
    @property
    def trademark(self):
        return self._trademark
    @trademark.setter
    def trademark(self,trademark):
        self. _trademark = trademark

    def __str__(self):
        return f'La marca es: {self._trademark} Es de tipo: {self._inputType}'

if __name__ == '__main__':
    input= InputDevice('Directa', 'sonic')
    print(input)
