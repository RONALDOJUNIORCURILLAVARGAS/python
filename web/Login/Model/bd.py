
import pymysql

def obtener_conexion():
    print("Conexion exitosa")
    return pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='prueba')
                                
    