#with open('prueba.txt', 'r', encoding='utf8') as file:
from ManejoArchivos import ManejoArchivos

with ManejoArchivos('prueba.txt') as file:
    print(file.read())