import sys
from psycopg2 import pool

class Conection:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CONECTION = 1
    _MAX_CONECTION = 5
    _pool = None

    @classmethod
    def get_pool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CONECTION, cls._MAX_CONECTION, host=cls._HOST, user=cls._USERNAME, password=cls._PASSWORD, port=cls._DB_PORT, database=cls._DATABASE)
                print(f'Conexión realizada correctamente')
                return cls._pool
            except Exception as e:
                print(f'Hubo un error en conexion: {e}')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def get_conection(cls):
        conection = cls.get_pool().getconn()
        print(f'Conexión obtenida')
        return conection

    @classmethod
    def release_conection(cls, conection):
        cls.get_pool().putconn(conection)
        print(f'Regresar conexion al pool')

    @classmethod
    def close_connections(cls):
        cls.get_pool().closeall()

if __name__ == '__main__':
    conexion = Conection.get_conection()
    Conection.release_conection(conexion)
    conexion2 = Conection.get_conection()
    conexion3 = Conection.get_conection()
    conexion4 = Conection.get_conection()
    conexion5 = Conection.get_conection()
    conexion6 = Conection.get_conection()
