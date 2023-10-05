from Conection import Conection
from logger_base import log
class CursorPool:
    def __init__(self):
        self._conection = None
        self._cursor = None

    def __enter__(self):
        log.debug('Inicio de metodo with __enter__')
        self._conection = Conection.get_conection()
        self._cursor = self._conection.cursor()
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        log. debug('Ejecuta metodo exit')
        if exc_val:
            self._conection.rollback()
            log.error(f'Ocurrio una excepcion: {exc_val} {exc_type}')
        else:
            self._conection.commit()
            log.debug('Commit de transaccion')
        self._cursor.close()
        Conection.release_conection(self._conection)
if __name__ == '__main__':
    with CursorPool() as cursor:
        log.debug('Dentro bloque with')
        cursor.execute('SELECT * FROM persona ORDER BY id')
        log.debug(cursor.fetchall())