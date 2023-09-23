try:
    #r de leer
    file = open('prueba.txt', 'r', encoding='utf8')
    #Muesra el archivo completo
    print(file.read())
    #Muestra solo una parte del archuvo print(file.read(7))
    #Leer lineas completas print(file(readline()))

    #crear copia de archivo
    file2 = open('copia.txt', 'a', encoding='utf8')
    file2.write(file.read())
    file2.close()
except Exception as e:
    print(e)