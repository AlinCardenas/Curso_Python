from Empleado import *
class Gerente(Empleado):
    def __init__(self,nombre,sueldo,departamento):
        super().__init__(nombre,sueldo)
        self.departamento = departamento

    def __str__(self):
      return f'{super().__str__()}, departamento: {self.departamento}'

