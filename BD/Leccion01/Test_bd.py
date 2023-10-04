import psycopg2
#generar conexión
conection = psycopg2.connect(user = 'postgres', password ='admin', host='127.0.0.1', port ='5432', database='test_db')

try:
    with conection:
        with conection.cursor() as cursor:
            #query = 'SELECT * FROM persona'
            #cursor.execute(query)
            #registros = cursor.fetchall()
            #print(registros)
            #Insertar registros a bd
            #query = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s,%s,%s)'
            #getData = (('Fernando', 'Ramirez', 'fernando@gmail.com'), ('Ricardo', 'Martiniez', 'ricardo@gmail.com'),('Juan','Mora', 'juan@gmail.com'))
            #cursor.executemany(query, getData)
            #registros = cursor.rowcount
            #print(f'Registro insertado: {registros}')
            #query = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id=%s'
            #datos = (('Carlos', 'Juarez', 'juan @gmail.com', 4), ('Oliver', 'Cardona', 'oliver@gmail.com',6))
            #cursor.executemany(query, datos)
            #show = 'SELECT * FROM persona'
            #cursor.execute(show)
            #showData = cursor.fetchall()
            #for data in showData:
            #    print(data)
            query = 'DELETE FROM persona WHERE id=%s'
            id = input('Ingresa id: ')
            values = (id,)
            cursor.execute(query,values)
            show = 'SELECT * FROM persona ORDER BY id'
            cursor.execute(show)
            showData = cursor.fetchall()
            for data in showData:
                print(data)

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conection.close()