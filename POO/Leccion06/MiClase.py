class MiClase:
    variable_clase = 'valor'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia
    #Metodos estaticos
    """Los metodos estaticos no pueden acceder a  las variables
    de instancia"""
    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)
    #metodos de clase
    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)
    def metodo_instancia(self):
        self.metodo_estatico()
        self.metodo_clase()

print(MiClase.variable_clase)
#asociar una nueva varible a la clase
print('Agregar variable de clase'.center(50,'-'))
MiClase.nueva_variable = 'variable 2'
print(MiClase.nueva_variable)

print('Generar instancia'.center(50,'-'))
miClase = MiClase('hola')

print('ingresar a metodo de clase desde objeto'.center(50,'-'))
miClase.metodo_clase()

print('ingresar a metodo estatico desde objeto'.center(50,'-'))
miClase.metodo_estatico()

print('ingresar a variable de instancia desde objeto'.center(50,'-'))
miClase.variable_instancia

print('ingresar a variable de clase desde objeto'.center(50,'-'))
print(miClase.nueva_variable)

print('accedder desde clase a metodos'.center(50,'-'))
MiClase.metodo_estatico()
MiClase.metodo_clase()
