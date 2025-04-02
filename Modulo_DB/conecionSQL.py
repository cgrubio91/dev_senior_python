import mysql.connector

# configuración de la CONEXION
conexion = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    password = "Cristian1991*",
    database = "academiadevsenior"
)

if conexion.is_connected():
    print("Conexión exitosa a la base de datos")
    ##cgrubio91/dev_senior_python/Modulo_DB/conecionSQL.py