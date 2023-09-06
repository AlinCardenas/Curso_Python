#definir funciones
def mi_funcion():
    print('estoy en funcion')

#hay dos tipos de datos que pueden entrar a una funcion, parametrso y argumentos
#los parametrso son las variables que se declaran en la funcion
#los argumentos son lo valores que se envian a la funcion

def names(name, apellido):
    print(f'mi nombre es {name} {apellido}')
names('Alin', 'Cardenas')

def suma(num1,num2):
    return num1+num2

resultado = suma(5,3)
print(f'El resultado es: {resultado}')


#Asignar valores por default a los parametros de la funcion
#def resta(a:int = 0, b:int =0)-> int: especifica que tipo de dato retornara
def resta(a=0, b=0):
    return a-b
print(f'El resultado de la resta es: {resta(0,0)}')
print(f'El resultado de la resta es: {resta(8,3)}')

#ingresar datos sin especificar el numero
#El tipo de dato que genera es una dupla
def listNames(*names):
    for name in names:
        print(name)
listNames('Alin','Carlos','Pedro','Juan')

# dejar entrar una lista de terminos a la funcion
# kwargs es para definir que estamos solicitando elementos clave valor
def listTerm(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}:{value}')
listTerm(IDE='hola', NOSE='hola2')

#funcion recursiva: funcion que se manda a llamar a si misma para completar una tarea
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)

print(factorial(5))




