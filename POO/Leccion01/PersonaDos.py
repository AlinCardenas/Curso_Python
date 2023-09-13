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
        self._age = age
    """los decoradores modifican el funcionamiento de metodos
    por esta razon el decorador property indica que el metodo
    name va arecuperar el nombre, estamos encapsulando"""
    @property
    def name(self):
        return self._name
    """metodo set para modificar nombre"""
    #metodo para modificar nombre, si no se quiere modificar no se crea el motodo
    @name.setter
    def name(self, name):
        self._name = name
    @property
    def lastName(self):
        return self.__lastName
    @lastName.setter
    def lastName(self, lastName):
        self.__lastName = lastName
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, age):
        self._age = age
    def show_detail(self):
        #solo si utilizo self puedo acceder al atributo
        print(f'{self._name} {self.__lastName} {self.age}')
    #Eliminaar objetos es un metodo destructor
    def __del__(self):
        print(f'Persona: {self._name} {self.__lastName}')
"""Para que no se ejecute este codigo en otros modulos
se puede realiza una validacion"""
if __name__ == '__main__':
    persona1 = PersonaDos('Alin', 'Cardenas', 20)
    #persona1.show_detail()
    print(persona1.name)
    #acceder a metodo para modifocar nombre
    persona1.name = 'Amparo'
    persona1.lastName = 'Marin'
    persona1. age = 21
    print(persona1.age)
    print(persona1.lastName)
    persona1.show_detail()
    """Si persona._nombre se conoce como atrubuto encapsulado
    es posible modificar el atributo pero no es recomendable
    si el atrubuto tiene doble guion bajo no es posible modificar fuera de la clase"""
    """Hay metodos set y get que permiten traer los atributos d la clase"""






