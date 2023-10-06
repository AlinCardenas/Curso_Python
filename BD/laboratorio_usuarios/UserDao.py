from CursorPool import CursorPool
import os
class UserDao:
    _SELECT = 'SELECT * FROM users WHERE id=%s'
    _SELECT_ALL = 'SELECT * FROM users ORDER BY id'
    _INSERT = 'INSERT INTO users(name, password) VALUES(%s,%s)'
    _UPDATE = 'UPDATE user SET name=%s, password=%s WHERE id=%s'
    _DELETE = 'DELETE FROM user WHERE id=%s'


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

user = UserDao.select_all()
print(user)