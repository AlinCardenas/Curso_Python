class PersonaDos:
    """El encapsulamiento es un mecanismo que consiste en organizar
    datos y metodos de una estructura, ocultando el stado interno de los
    objetos y controlando el acceso a sus propidades y metodos"""

    def __init__(self, name, lastName, age):
        #Una forma de restringir el acceso a atrubutos es usando_
        """Con _ indicamos que no puede acceder directamente
         al valor del atributo y solo la misma clase puede acceder"""
        self._name = name
        """Si se quiere ser mas restrictivo ingresar __"""
        self.__lastName = lastName
        self.age = age
    def show_detail(self):
        #solo si utilizo self puedo acceder al atributo
        print(f'{self._name} {self.__lastName} {self.age}')

persona1 = PersonaDos('Alin', 'Cardenas', 20)
persona1.show_detail()
"""Si persona._nombre se conoce como atrubuto encapsulado
es posible modificar el atributo pero no es recomendable
si el atrubuto tiene doble guion bajo no es posible modificar fuera de la clase"""







