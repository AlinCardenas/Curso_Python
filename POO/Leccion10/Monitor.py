class Monitor:
    countMonitors = 0
    def __init__(self, trademark, size):
        Monitor.countMonitors += 1
        self.idMonitor = Monitor.countMonitors
        self._trademark = trademark
        self._size = size
    @property
    def trademark(self):
        return self._trademark
    @trademark.setter
    def trademark(self, trademark):
        self._trademark = trademark
    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size):
        self._size = self.size
    def __str__(self):
        return f'El id es: {self.idMonitor} La marca es:{self._trademark} El tamaño es: {self._size}'

if __name__ == '__main__':
    monitor = Monitor('dell', 'grande')
    print(monitor)
