from Clase_conexion import Conexion
from Clase_producto import Producto


class Metodos:

#   Metodo total inventario ligado a listar
    @classmethod
    def valor_total_inventario(cls, datos_producto):
        productos = datos_producto
        total = 0
        for producto in productos:
            total += producto.precio * producto.stock

        print(f'El valor total del inventario actual es: ${total:.1f}')
        return total