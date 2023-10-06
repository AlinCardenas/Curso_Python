class User:
    def __init__(self, id_user=None, name=None, password=None):
        self.id_user = id_user
        self.name = name
        self.password = password

    def __str__(self):
        return (f'Id: {self.id_user} Nombre: {self.name} Contraseña: {self._password}')

    @property
    def id_user(self):
        return self._id_user
    @id_user.setter
    def id_user(self, id_user):
        self._id_user = id_user
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name
    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, password):
        self._password = password

if __name__ == '__main__':
    name = input('Ingresa nombre: ')
    password = input('ingresa contraseña: ')
    user = User(name=name, password=password)
    print(user)