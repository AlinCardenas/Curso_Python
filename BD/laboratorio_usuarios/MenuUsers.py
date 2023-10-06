class MenuUsers:
    _Option = None

    while _Option is None:
        print('''
        1. Listar usuarios
        2. Agregar usuario
        3. Actualizar usuario
        4. Eliminar usuario
        ''')
        _Option = input('Ingresa una opcion: ')
        if _Option == 1:
            print('hola')
        elif _Option == 2:
            print('')
