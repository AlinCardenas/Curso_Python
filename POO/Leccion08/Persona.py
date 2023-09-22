class Persona:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __add__(self, other):
        return f'{self.name} {other.name}'
    def __sub__(self, other):
        return f'{self.age - other.age}'

persona = Persona('Alin', 20)
persona1 = Persona('Alin2', 10)
print(persona + persona1)
print(persona - persona1)
#obj1 + obj2
#obj1.__add__(obj2)