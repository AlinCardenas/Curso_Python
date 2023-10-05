from Conection import Conection
from Person import Person
from logger_base import log
from CursorPool import CursorPool

class PersonDAO:
    '''DAO = Data acces object'''
    _SELECT = 'SELECT * FROM persona ORDER BY id'
    _INSERT = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s,%s,%s)'
    _UPDATE = 'UPDATE persona SET nombre=%s, apellido= %s, email=%s WHERE id= %s '
    _DELETE = 'DELETE FROM persona WHERE id=%s'

    @classmethod
    def select(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELECT)
            get_users = cursor.fetchall()
            people = []
            for data in get_users:
                person = Person(data[0], data[1], data[2], data[3])
                people.append(person)
            return people
    @classmethod
    def insert(cls, person):
        with CursorPool() as cursor:
            values = (person.name, person.last_name, person.email)
            cursor.execute(cls._INSERT, values)
            log.debug(f'Registro insertado: {person}')
            return cursor.rowcount
    @classmethod
    def update(cls, person):
        with CursorPool() as cursor:
            values = (person.name, person.last_name, person.email, person.id_person)
            cursor.execute(cls._UPDATE, values)
            log.debug(f'Registro actualizado: {person}')
            return cursor.rowcount
    @classmethod
    def delete(cls, person):
        with CursorPool() as cursor:
            values = (person.id_person, )
            cursor.execute(cls._DELETE, values)
            log.debug(f'Registro eliminado:{person}')
            return cursor.rowcount

if __name__ == '__main__':
    #insertar
    # persona = Person(name='Ricardo', last_name='Juarez', email= 'ricardo@gmail.com' )
    # person_inset = PersonDAO.insert(persona)
    # Actualizar
    # persona = Person(16,'Carla','Mora','rocio@gmail.com')
    # peson_update= PersonDAO.update(persona)
    # delete
    #persona = Person(id_person=16)
    #person_delete = PersonDAO.delete(persona)
    #ver objetos
    people = PersonDAO.select()
    for person in people:
        log.debug(person)

