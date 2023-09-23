from domain.Movie import Movie
from service.MovieCatalog import MovieCatalog

option = None
while option !=4:
    try:
        print('Opciones:')
        print('1. Agregar ')
        print('2. Listar')
        print('3. Eliminar')
        print('4. Salir')
        option = int(input('Ingresa opción '))
        if option == 1:
            nameMovie = input('Ingrese un nombre')
            pelicula = Movie(nameMovie)
            MovieCatalog.add_movie(pelicula)
        elif option == 2:
            MovieCatalog.list_movies()
        elif option == 3:
            MovieCatalog.delete_movies()

    except Exception as e:
        print(f'Ocurrio un error {e}')
        option = None
else:
    print('Saliendo ...')
