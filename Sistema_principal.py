from Clase_producto import Producto

class Sistema:

    @classmethod
    def info_agregar_producto(cls):
        while True:
            try:
                nombre_producto = input('Ingrese el nombre del producto: ').strip().title()
                precio_producto = float(input('Ingrese el precio total del producto: '))
                stock_producto = int(input('Ingrese la cantidad total en stock: '))

                if precio_producto > 0 and stock_producto > 0:
                    producto_recibido = Producto(nombre=nombre_producto, precio=precio_producto, stock=stock_producto)
                    return producto_recibido
                elif precio_producto <= 0:
                    print('El precio del producto debe ser mayor a 0')
                    print()
                elif stock_producto <= 0:
                    print('El stock del producto debe ser mayor a 0')
                    print()
                else:
                    print('Datos invalidos, ingrese nuevamente!!')
                    print()
            except ValueError:
                print('El valor ingresado debe ser numero entero!!')
                print()

    @classmethod
    def solicitar_nombre_producto(cls):
        while True:
            nombre_producto = input('Ingrese el nombre del producto que desea buscar: ').strip().title()

            if nombre_producto:
                return nombre_producto 
            
            print('El nombre puede estar vacío!!')

    @classmethod
    def solicitar_datos_actualizar(cls):
        while True:
            try:
                id_producto = int(input('Ingrese el id del producto a actualizar: '))
                nuevo_stock = int(input('Ingresa el nuevo valor del stock: '))
                datos_producto = Producto(id_producto=id_producto, stock=nuevo_stock)

                return datos_producto 
            
            except ValueError:
                print('Por favor ingrese un valor numerico.')
                print()  

    @classmethod
    def solicitar_producto_eliminar(cls):
        while True:
            try:
                id_producto = int(input('Ingrese el id del producto que desea elminar: '))
                datos_eliminar = Producto(id_producto=id_producto)

                return datos_eliminar
            
            except ValueError:
                print('Por favor ingrese un valor numerico.')
                print()     
