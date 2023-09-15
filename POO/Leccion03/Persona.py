class Persona:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f'Persona: {self.name} {self.age}'
"""Definir clase hija,
class Name(nombre clase padre)"""
class Empleado(Persona):
    def __init__(self, name, age, salary):
        #metodo para acceder a metodos de clase padre super()
        super().__init__(name, age)
        self.salary = salary
    def __str__(self):
        return f'{super().__str__()} {self.salary}'