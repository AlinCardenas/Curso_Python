from Conection import Conection
class CursorPool:
    def __init__(self):
        self._conection = None
        self._cursor = None

    def __enter__(self):
        self._conection = Conection.get_conection()
        self._cursor = self._conection.cursor()
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            self._conection.rollback()
            print(f'Ourrio un error:{exc_val} {exc_type}')
        else:
            self._conection.commit()
            print(f'Commit realizado')
        self._conection.close()
        Conection.release_conection(self._conection)

if __name__ == '__main__':
    with CursorPool() as cursor:
        print('Dentro bloque with')
        cursor.execute('SELECT * FROM persona ORDER BY id')
        print(cursor.fetchall())