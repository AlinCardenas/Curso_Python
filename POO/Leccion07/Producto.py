class Producto:
    contador_productos = 0
    @classmethod
    def contar_productos(cls):
        cls.contador_productos += 1
        return cls.contador_productos

    def __init__(self, nombre, precio):
        self._id_producto = Producto.contar_productos()
        self._nombre = nombre
        self._precio = precio

    @property
    def id_producto(self):
        return self._id_producto
    @id_producto.setter
    def id_producto(self, id_producto):
        self._id_producto = id_producto

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def precio(self):
        return  self._precio
    @precio.setter
    def precio(self, precio):
        self._precio = precio

    def __str__(self):
        return f'Producto: Id: {self._id_producto}, Nombre: {self._nombre}, Precio:{self._precio}'

if __name__ == '__main__':
    producto = Producto('papas', 89.3)
    print(producto)
    producto2 = Producto('papotas', 89.3)
    print(producto2)