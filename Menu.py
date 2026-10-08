from ClaseDAO import DAO
from Metodos_adicionales import Metodos
from Sistema_principal import Sistema

class Menu:

    #   Metodo mostrar recorrido for para el metodo SELECT
    @classmethod
    def mostrar_productos(cls, lista):
        for valor in lista:
            print(f'''Id: {valor.id_producto} | Nombre: {valor.nombre} | Precio: {valor.precio} | Stock: {valor.stock}''')

    @classmethod
    def menu_opciones(cls):
        print('''\t\n--- Sistema Productos ---
        \nSeleccione una opcion:
    1. Agregar producto
    2. Listar productos
    3. Buscar producto por nombre
    4. Actualizar stock
    5. Eliminar producto
    6. Valor total inventario
    7. Salir''') 

    @classmethod
    def seleccionar_opcion(cls):
        opcion = None
        while opcion != 7:
            try:
                print('-----------------------------------------------------')
                Menu.menu_opciones()
                opcion = int(input('\nIngrese la opcion que desea: '))

                if opcion == 1:
                    print()
                    datos_producto = Sistema.info_agregar_producto()
                    DAO.agregar_productos(datos_producto)
                elif opcion == 2:
                    listar_productos = DAO.listar_productos()
                    print('\nProductos actuales en la tienda: \n')
                    Metodos.mostrar_productos(listar_productos)
                elif opcion == 3:
                    nombre_producto = Sistema.solicitar_nombre_producto()
                    listar_productos = DAO.buscar_producto(nombre_producto)
                    Menu.mostrar_productos(listar_productos)
                elif opcion == 4:
                    print()
                    datos_actualizar = Sistema.solicitar_datos_actualizar()
                    respuesta = DAO.actualizar_stock(datos_actualizar)
                    print(respuesta)
                elif opcion == 5:
                    print()
                    datos_eliminar = Sistema.solicitar_producto_eliminar()
                    eliminar_producto = DAO.eliminar_producto(datos_eliminar)
                    print(eliminar_producto)
                elif opcion == 6:
                    print()
                    productos = DAO.listar_productos()
                    Metodos.valor_total_inventario(productos)
                elif opcion == 7:
                    print()
                    print('Gracias por usar el programa... Saliendo!')
                    break
                else:
                    print('\nSeleccione una opcion valida!!')

            except ValueError as e:
                print(f'\nDebe ingresar un numero entero!!')

Menu.seleccionar_opcion()