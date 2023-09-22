from Empleado import Empleado
from Gerente import Gerente


def show_detail(objeto):
    print(objeto)
    print(type(objeto))
    if isinstance(objeto, Gerente):
        print(objeto.departamento)

empleado= Empleado('Luis',3500)
show_detail(empleado)
gerente = Gerente('roberto', 5000, 'BD')
show_detail(gerente)