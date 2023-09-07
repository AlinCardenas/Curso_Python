class Persona:
    #cuando se define una clase lo prinero que se hace es
    #1. Declarar clase
    #2. Definir atributos
    #3. Crear metodos
    #el metodo inicializa la clase y declara atributos,el self crea la referecia del objeto
    #def __init__(self):
        #Declarar atributos
        #self.name = 'Alin'
        #self.lastName = 'Cardenas'
        #self.age = 20
    #els self sepuede camiar por otro nombre como this, pero se recommienda usar self
    def __init__(self, name, lastName, age):
        #el parametro puede tener nombre diferente del atributo
        #atributo = parametro
        self.name = name
        self.lastName = lastName
        self.age = age

    def show_detail(self):
        print(f'{self.name} {self.lastName} {self.age}')

#Crear instancia de la clase variable = className()
persona1 = Persona('Alin', 'Cardenas', 20)
#cambiar los valores del objeto  ya creado persona1.name = 'Alin2'
#Acceder directamente a los elementos de la clase print(f'{persona1.name} {persona1.lastName} {persona1.age}')
#Llamar metodo de la clase Persona
persona1.show_detail()
persona2 = Persona('Carlos', 'Lopez', 45)
#agregar nuevo atributo a la instancia
persona2.phone = 1234
#se puede acceder a metodos de la clase directamete nameClass.nameMethod(self)
Persona.show_detail(persona2)
print(persona2.phone)




