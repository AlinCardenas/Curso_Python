from logger_base import log
import psycopg2
import sys
class Conection:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _conection = None
    _cursor = None

    @classmethod
    def create_conection(cls):
        if cls._conection is None:
            try:
                cls._conection = psycopg2.connect(host=cls._HOST, user=cls._USERNAME, password=cls._PASSWORD, port=cls._DB_PORT, database=cls._DATABASE)
                log.debug(f'Conexion exitosa {cls._conection}')
                return cls._conection
            except Exception as e:
                log.error(f'Ocurrio un error en la conexión: {e}')
                sys.exit()
        else:
            return cls._conection
    @classmethod
    def get_cursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.create_conection().cursor()
                log.debug(f'Se abrio el cursor: {cls._cursor}')
                return cls._cursor
            except Exception as e:
                log.error(f'Ocurrio un error en obtener cursor: {e}')
                sys.exit()
        else:
            return cls._cursor

if __name__ == '__main__':
    Conection.create_conection()
    Conection.get_cursor()
