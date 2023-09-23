import os
class MovieCatalog:
    filePath = 'peliculas.txt'

    @classmethod
    def add_movie(cls, movie):
        with open(cls.filePath, 'a', encoding='utf8') as file:
           file.write(f'{movie.name}\n')
    @classmethod
    def list_movies(cls):
        with open(cls.filePath,'r', encoding='utf8') as file:
            print('Catálogo'. center(50,'-'))
            print(file.read())
    @classmethod
    def delete_movies(cls):
        os.remove(cls.filePath)
        print(f'archivo eliminado: {cls.filePath}')