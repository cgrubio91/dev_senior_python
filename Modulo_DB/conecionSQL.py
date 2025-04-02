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

# Insertar datos(INSERT)
query = "INSERT INTO Profesores(nombre,especialidad,experiencia) VALUES(%s, %s, %s);"
valores = ("Juan David", "Ingenieria de Sistemas", 5)
cursos.execute(query, valores)
conexion.commit() # Guardar los cambios

# Actualizar(UPDATE)
query = "UPDATE profesores SET experiencia = %s WHERE id_profesor = %s"
valores = (7, 12)  
cursos.execute(query,valores)
conexion.commit() # Guardar los cambios
print(f"Fila insertada: {cursos.rowcount}")

# Eliminar(DELETE)
query = "DELETE FROM profesores WHERE id_profesor =%s;"
valores = (14,)  
cursos.execute(query,valores)
conexion.commit() # Guardar los cambios
print(f"Fila insertada: {cursos.rowcount}")