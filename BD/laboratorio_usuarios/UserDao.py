import logging
from CursorPool import CursorPool
import MenuUsers
from User import User
import os
class UserDao:

    _SELECT = 'SELECT * FROM users WHERE id=%s'
    _SELECT_ALL = 'SELECT * FROM users ORDER BY id'
    _INSERT = 'INSERT INTO users(username, password) VALUES(%s,%s)'
    _UPDATE = 'UPDATE users SET username=%s, password=%s WHERE id=%s'
    _DELETE = 'DELETE FROM users WHERE id=%s'

    @classmethod
    def select(cls):
        id = tuple(input('Ingresa el id del usuario que desea visualizar: '))
        with CursorPool() as cursor:
            cursor.execute(cls._SELECT, id)
            get_user = cursor.fetchone()
            if get_user:
                print(f'''
                Id: {get_user[0]}
                Nombre: {get_user[1]}
                Password:{get_user[2]}
                ''')
            else:
                print('Usuario no encontrado intenta nuevamente')
                UserDao.select()

    @classmethod
    def select_all(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELECT_ALL)
            get_users = cursor.fetchall()
            list_users = []
            for user in get_users:
                order_users =  user_dict = {
                    'id': user[0],
                    'name': user[1],
                    'password': user[2]
                }
                list_users.append(order_users)
            return list_users

    @classmethod
    def add_user(cls):
        with CursorPool() as cursor:
            name = input('Ingresa nombre: ')
            password = input('Ingresa contraseña: ')
            data = (name, password)
            cursor.execute(cls._INSERT, data)
            print(f'Registro insertado')
            return cursor.rowcount

    @classmethod
    def update_name(cls):
        with CursorPool() as cursor:
            id_user = tuple(input('Ingresa id de usuario: '))
            cursor.execute(cls._SELECT, id_user)
            search_user = cursor.fetchone()
            if search_user:
                new_name = input('Ingresa nuevo nombre: ')
                cursor.execute('UPDATE users SET username=%s WHERE id=%s', (new_name, id_user))
                print(f'Nombre Actualizado por: {new_name}')
            else:
                print('Id no encontrado, intenta nuevamente')
                UserDao.update_user()

    @classmethod
    def update_password(cls):
        with CursorPool() as cursor:
            id_user = tuple(input('Ingresa id de usuario: '))
            cursor.execute(cls._SELECT, id_user)
            search_user = cursor.fetchone()
            if search_user:
                new_password = input('Ingresa nueva contraseña: ')
                cursor.execute('UPDATE users SET password=%s WHERE id=%s', (new_password, id_user))
                print(f'Contraseña Actualizada por: {new_password}')
            else:
                print('Id no encontrado, intenta nuevamente')
                UserDao.update_user()

    @classmethod
    def update_all(cls):
        with CursorPool() as cursor:
            id_user = tuple(input('Ingresa id: '))
            cursor.execute(cls._SELECT, id_user)
            search_user = cursor.fetchone()
            if search_user:
                new_name = input('Ingresa nuevo nombre: ')
                new_password = input('Ingresa nueva contraseña: ')
                cursor.execute(cls._UPDATE, (new_name, new_password, id_user))
                print(f'Datos Actualizados: {new_name} {new_password}')

    @classmethod
    def update_user(cls):
        option = int(input('''Ingresa opcion
        1. Actualizar nombre
        2. Actualizar contraseña
        3. Actualizar nombre y contraseña
        '''))
        if option == 1:
            UserDao.update_name()
        elif option == 2:
            UserDao.update_password()
        elif option == 3:
            UserDao.update_all()

    @classmethod
    def delete_user(cls):
        with CursorPool() as cursor:
            id_user = tuple(input('Ingresa el id de usuario que desea eliminar: '))
            if id_user:
                option = int(input(f'''Esta seguro que desea eliminar el usuario {id_user}
                1. Si
                2. No
                '''))
                if option == 1:
                    cursor.execute(cls._DELETE, id_user)
                    print('Registro eliminado')
                else:
                    MenuUsers
