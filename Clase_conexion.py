from psycopg2 import pool
from psycopg2 import Error
from dotenv import load_dotenv
import os

load_dotenv()

class Conexion:

    USER = 'postgres'
    HOST = 'localhost'
    NAME_DB = 'producto'
    PASSWORD = os.getenv("PASSWORD")
    PORT_DB = 5432
    MIN_CONEX = 1
    MAX_CONEX = 5
    POOL_NAME = 'clienete_producto_connect'
    pool = None

    @classmethod
    def obtener_pool(cls):
        if cls.pool is None:
            try:
                cls.pool = pool.ThreadedConnectionPool(
                    minconn = cls.MIN_CONEX,
                    maxconn = cls.MAX_CONEX,
                    user = cls.USER,
                    host = cls.HOST,
                    database = cls.NAME_DB,
                    password = cls.PASSWORD,
                    port = cls.PORT_DB
                    )
                return cls.pool
            except Error as e:
                print(f'Ocurrio un error al obtener POOL: {e}')
                return None
            except Exception:
                print(f'Error: {Exception}')
                return None
        else:
            return cls.pool

    @classmethod
    def obtener_conexion(cls):
        p = cls.obtener_pool()
        if p is not None:
            return p.getconn()
        return None

    @classmethod
    def liberar_conexion(cls, conexion):   
        if cls.pool is None:
            print('El pool no ha sido inicializado!!')
            return
        if conexion:
            cls.pool.putconn(conexion)