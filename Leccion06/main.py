#Listas
names = ['carla', 'juan','ricadro','pedro']
print(names)
#acceder a elementos de forma individual
#nombre_lista[posicion]
print(names[0])
##acceder a elementos de manera inversa
print(names[-1])
#obtener numero de elementos en la lista con funcion len
print(len(names))
#agregar elementos a la lista con funcion append
names. append('Paola')
print(names)
#insertar elemento en indice especifico
#nombre_lista.inser(posocion,'Elemento_agregado')
names.insert(2,'Roberto')
print(names)
#remover elemento de la lista
#nombre_lista. remove('Valor')
names.remove('Paola')
print(names)
##rmover ultomo valor agregado a la lsita
names.pop()
print(names)
#Eliminar elemento en un indice indicado
#del names[0]
#print(names)
#Limpiar todos los elementos de la lista
#names.clear()
#print(names)
##borrar lista pos completo con del nombre de lsita

#acceder a rango de elementos de una lsita
print(names[0:2]) #sin incluir el indice 2
#Ir desde el inicisio de la lsita al indice(sin incluirlo}9
print(names[:3])

##Modifocar valor especificando un indice
names[2]='Luis'
print(names)
for name in names:
    print(name)
else:
    print('no hay mas nombres')


##Las tuplas guardan el orden de los elementos y no se puede modificar
##Es unca coleccion inmutable
frutas = ('naranja', 'platano', 'Guayaba')
print(frutas[1])
print(frutas[-1])
print(frutas[0:2])
for fruta in frutas:
    print(fruta, end=' ')
##Pasar tupla a lista
frutaList = list(frutas)
print(frutaList)
frutaList[0]= 'guayaba'
frutas = tuple( frutaList)
print('\n', frutas)
##Set no mantiene un orden y tampoco permite almacenar elementos duplicados
#No es posible modificar elementos, pero si agregar y eliminar
planetas = {'Marte', 'Venus', 'Jupiter'}
print(planetas)
#revisar si hay un elemento presente en set
print('Marte' in planetas)
planetas.add('Tierra')
print(planetas)
planetas.remove('Marte')
print(planetas)
#Elimiar elemetos sin retornar erro si no existe
planetas.discard('Marte')
#Limpiar todos los elementos con crear()
#Diccionaario, se compone de (key, value)
diccionario = {
    'IDE': 'Integrated Development Environment',
    'OOP': 'Object Oriented Programming',
    'DBMS': 'Database Management System'
}
print(diccionario)
print(diccionario['IDE'])
#Otra forma de obtener datos de diccionario
print(diccionario.get('OOP'))
#odificar elemetos
diccionario['IDE'] ='Estas es prueba '
print(diccionario)
##obtiene la llave y el valor
for key, value in diccionario.items():
    print(key, value)
#obtiene solo las llaves
for key in diccionario.keys():
    print(key)
#obtener unicamente los valore
for value in diccionario.values():
    print(value)
#compobar si existe valor en diccionario
print('IDE' in diccionario)



