#open() abrir o crear achivo
try:
    #open('nameFile', 'W' (de escritura), encoding='utf8' para aceptar acentos)
    file = open('prueba.txt', 'w', encoding='utf8')
    #Escrinir informacion
    file.write('Hola, esto es una prueba\n')
    file.write('Otra linea\n')
    file.write('Información con acentos\n')

except Exception as e:
    print(e)
finally:
    #despues de cerrar el archivo ya nose puede agregar informacion abajo de esta linea
    file.close()
    print('Archivo cerrado ')