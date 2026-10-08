from Clase_producto import Producto
from Clase_conexion import Conexion

class DAO:

    SELECT = 'SELECT * FROM inventario ORDER BY id_producto'
    INSERTAR = 'INSERT INTO inventario (nombre, precio, stock) VALUES (%s, %s, %s)'
    ACTUALIZAR = 'UPDATE inventario SET stock = %s WHERE id_producto = %s;'
    ELIMINAR = 'DELETE FROM inventario WHERE id_producto = %s'
    BUSCAR = 'SELECT id_producto, nombre, precio, stock FROM inventario WHERE nombre = %s'


#   Metodo agregar (Crear) producto
    @classmethod
    def agregar_productos(cls, datos_producto):
        conexion = Conexion.obtener_conexion()
        cursor = None
        registros_insertados = 0
    
        if conexion is not None:
            try:
                cursor = conexion.cursor()
                valores = (datos_producto.nombre, datos_producto.precio, datos_producto.stock)
                cursor.execute(cls.INSERTAR, valores)
                conexion.commit()
    
                registros_insertados = cursor.rowcount
                print(f'Productos agregados: {registros_insertados}')
                    
            except Exception as e:
                print(f'Ocurrio un error al agregar el producto: {e}')
            finally:
                if cursor is not None:
                    cursor.close()
                if conexion is not None:
                    Conexion.liberar_conexion(conexion)
        else:
            print('No se pudo conectar con la base de datos!!')
    
        return registros_insertados


#   Metodo listar (Leer) producto
    @classmethod
    def listar_productos(cls):
        productos = []
        conexion = Conexion.obtener_conexion()
        cursor = None
        if conexion is not None:
            try:
                cursor = conexion.cursor()
                cursor.execute(cls.SELECT)
                resultados = cursor.fetchall()
    
                for datos in resultados:
                    id_producto, nombre, precio, stock = datos
                    producto = Producto(id_producto, nombre, precio, stock)
                    productos.append(producto)
    
            except Exception as e:
                print(f'Ocurrio un error al listar los productos: {e}')
            finally:
                if cursor is not None:
                    cursor.close()
                if conexion is not None:
                    Conexion.liberar_conexion(conexion)
        else:
            print('No se pudo conectar con la base de datos!!')
        
        return productos

# Metodo buscar productos
    @classmethod
    def buscar_producto(cls, nombre_producto):
        productos = []
        conexion = Conexion.obtener_conexion()
        cursor = None
        if conexion is not None:
            try:
                cursor = conexion.cursor()
                valores = (nombre_producto,)
                cursor.execute(cls.BUSCAR, valores)
                resultados = cursor.fetchall()

                if len(resultados) == 0:
                    print('Advertencia: No se encuentra ningun producto relacionado!!')

                for datos in resultados:
                    id_producto, nombre, precio, stock = datos
                    producto = Producto(id_producto, nombre, precio, stock)
                    productos.append(producto)

            except Exception as e:
                print(f'Ocurrio un error al buscar el producto: {e}')
            finally:
                if cursor is not None:
                    cursor.close()
                if conexion is not None:
                    Conexion.liberar_conexion(conexion)            
        else:
            print('No se pudo conectar con la base de datos!!')

        return productos


#   Metodo actualizar producto
    @classmethod
    def actualizar_stock(cls, datos_producto):
        conexion = Conexion.obtener_conexion()
        cursor = None
        registros_actualizados = 0
        if conexion is not None:
            try:
                cursor = conexion.cursor()
                valores = (datos_producto.stock, datos_producto.id_producto)
                cursor.execute(cls.ACTUALIZAR, valores)
                conexion.commit()
    
                registros_actualizados = cursor.rowcount
                if registros_actualizados == 0:
                    print('El id que deseas actualizar no existe!!')
                else:
                    print(f'Productos actualizados: {registros_actualizados}')
    
            except Exception as e:
                print(f'Ocurrio un error al actualizar el stock del producto: {e}')
            finally:
                if cursor is not None:
                    cursor.close()
                if conexion is not None:
                    Conexion.liberar_conexion(conexion)
        else:
            print('No se pudo conectar con la base de datos!!')
    
        return registros_actualizados

# Metodo eliminar producto
    @classmethod
    def eliminar_producto(cls, producto_eliminar):
        conexion = Conexion.obtener_conexion()
        cursor = None
        eliminados = 0
        if conexion is not None:
            try:
                cursor = conexion.cursor()
                valores = (producto_eliminar.id_producto,)
                cursor.execute(cls.ELIMINAR, valores)
                conexion.commit()
                eliminados = cursor.rowcount
    
                if eliminados == 0:
                    print('El producto no existe...')
                else:
                    print(f'Se elimino con exito el producto!!')

            except Exception as e:
                print(f'Ocurrio un error al eliminar el producto: {e}')
            finally:
                if cursor is not None:
                    cursor.close()
                if conexion is not None:
                    Conexion.liberar_conexion(conexion)
        else:
            print('No se pudo conectar con la base de datos!!')
    
        return eliminados