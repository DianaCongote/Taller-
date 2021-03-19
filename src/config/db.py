import mariadb
from os import path
import json
import src.config.globals as globals

CONEXION_PATH = path.abspath('src/config/conexion.json')


def mostrarbd():
    conn = mysql.connector.connect (user='usuario', password='contraseña', host='host', port='puerto' )

    cursor = conn.cursor()

    databases = ("show databases")

    cursor.execute(databases)

    for (databases) in cursor:
        print databases[0]

