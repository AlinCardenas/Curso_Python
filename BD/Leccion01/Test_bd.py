import psycopg2
#generar conexión
conection = psycopg2.connect(user = 'postgres', password ='admin', host='127.0.0.1', port ='5432', database='test_db')

try:
    with conection:
        with conection.cursor() as cursor:
            query = 'SELECT * FROM persona'
            cursor.execute(query)
            registros = cursor.fetchall()
            print(registros)
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conection.close()


