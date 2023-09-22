from Monitor import Monitor
from Mouse import Mouse
from Keyboard import Keyboard


class Computer:
    countComputers = 0
    def __init__(self, name, monitor, keyboard, mouse):
        Computer.countComputers += 1
        self._idComputer = Computer.countComputers
        self._name = name
        self._monitor = monitor
        self._keyboard = keyboard
        self._mouse = mouse
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name = name
    @property
    def monitor(self):
        return self._monitor
    @monitor.setter
    def monitor(self,monitor):
        self._monitor = monitor
    @property
    def keyboard(self):
        return  self._keyboard
    @keyboard.setter
    def keyboard(self,keyboard):
        self._keyboard = keyboard
    @property
    def mouse(self):
        return self._mouse
    @mouse.setter
    def mouse(self, mouse):
        self._mouse = mouse

    def __str__(self):
        return f"""{self._name} : {self._idComputer}\nMonitor: {self._monitor}\nTeclado: {self._keyboard}\nRaton: {self._mouse}"""

if __name__ == '__main__':
    teclado = Keyboard('USB', 'Hp')
    mouse = Mouse('USB', 'Samsung')
    monitor = Monitor('VGA', '1')
    computadora = Computer('Computadora', monitor, teclado, mouse)
    print(computadora)
