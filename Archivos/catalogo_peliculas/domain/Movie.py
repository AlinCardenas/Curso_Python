class Movie:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return f'{self.name}'
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

if __name__ == '__main__':
    pelicula = Movie('jfhjs')

    n=5
    dataList= []
    var = []
    newData=''
    for num in range(1,n+1,1):
        print(num, end='')





