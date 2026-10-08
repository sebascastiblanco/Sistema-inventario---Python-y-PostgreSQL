class Producto:

    def __init__(self, id_producto=None, nombre=None, precio=None, stock=None):
        self.id_producto = id_producto
        self.nombre = nombre
        self.__precio = precio
        self.stock = stock

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, precio):
        self.__precio = precio

    def __str__(self):
        return f'Id: {self.id_producto}, Nombre: {self.nombre}, Precio: {self.precio}, Stock: {self.stock}'
