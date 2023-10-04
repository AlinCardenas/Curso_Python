import  psycopg2

conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432',database='test_db')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
            valores = ('Carla', 'Cerillo', 'rosa@gmail.com')
            cursor.execute(sentencia, valores)
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id=%s'
            valores = ('Fernada', 'Gonzalez', 'carla@gmail.com', 11)
except Exception as e:
    print(e)
finally:
    conexion.close()
    print('Transaccion terminada')

