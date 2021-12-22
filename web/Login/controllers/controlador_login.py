from logging import NullHandler
from Model.bd import obtener_conexion


def obtener_usuario(contraseña,correo):
    conexion= obtener_conexion()
    lista = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, nombre, correo FROM usuarios WHERE contraseña= %s AND correo= %s ",
                        (contraseña,correo,))
        #Se utiliza Fetchone para enlistar en un arreglo
        #y no fetchall porque crearia tuplas
        lista=cursor.fetchone()
        
        print(lista)
  
    conexion.commit()
    conexion.close()

    return lista
