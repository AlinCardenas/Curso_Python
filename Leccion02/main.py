firstNumber = int(input("Ingresa un numero "))
secondNumber = int(input("Ingrese segundo numero "))
suma = firstNumber + secondNumber
#print('RESULTADO:', suma)
#Operadores aritmeticos
print(f'El resultado de las suma es: {suma}')
resta = firstNumber-secondNumber
print(f'El resultado de la resta es: {resta}')
multiplicacion = firstNumber * secondNumber
print(f'El resultado de la multiplicaion es: {multiplicacion}')
#regresa valores de tipo flotante
division = firstNumber / secondNumber
print(f'El resultado de la division es: {division}')
#regesa valores de tipo entero
division = firstNumber // secondNumber
print(f'El valor entero de division es: {division}')
modulo = firstNumber % secondNumber
print(f'El residuo es: {modulo}')
exponente = firstNumber ** secondNumber
print(f'El esponente es: {exponente}')

#Operadores de asignacion
value = 10
print(value)
#incremento con reasignación, se puede usar con cualquier operador aritmetico
value += 1
print(value)

#Operadores de comparacion
a = 5
b = 8
c= 10
result = a==b
print(f'Las variables son iguales: {result}')
result = a!=b
print(f'Las variables son diferentes: {result}')

#operadores logicos
a = False
b = True

result = a and b
print(result)
result = a or b
print(result)
result = not a
print(result)

num= int(input('Ingresa un numero'))
if num>=0 and num<=5:
    print(f'El numero {num} se encuentra dentro del rango')
else:
    print(f'El numero {num} se encuentra dentro del rango')






