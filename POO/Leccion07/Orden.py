from Producto import *
class Orden:
    contador_ordenes = 0
    @classmethod
    def contar_ordenes(cls):
        cls.contador_ordenes += 1
        return cls.contador_ordenes

    def __init__(self, productos):
        self._id_ordenes = Orden.contar_ordenes()
        self._productos = list(productos)

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def calcular_total(self):
        total = 0
        for producto in self._productos:
            total += producto.precio
        return total

    @property
    def id_ordenes(self):
        return self._id_ordenes
    @id_ordenes.setter
    def id_ordenes(self, id_ordenes):
        self._id_ordenes = id_ordenes

    @property
    def productos(self):
        return self._productos
    @productos.setter
    def productos(self, productos):
        self._productos = productos
    def __str__(self):
        productos_str = ''
        for producto in self._productos:
            productos_str += producto.__str__() + '|'

        return f'orden: {self._id_ordenes}, Lista: {productos_str}'

if __name__ == '__main__':
    producto = Producto('papas', 89.3)
    producto2 = Producto('papotas', 89.3)
    productos =[producto, producto2]
    orden = Orden(productos)
    print(orden)
    producto3 = Producto('papas', 89.3)
    producto4 = Producto('papotas', 89.3)
    productos = [producto3, producto4]
    orden2 = Orden(productos)
    print(orden2)
    print( orden2.calcular_total())

