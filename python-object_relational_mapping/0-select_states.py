#!/usr/bin/python3
# Lists all states from the database hbtn_0e_0_usa.
# by Stefano Madueno
import sys
import MySQLdb

def list_states(username, password, database):
    # Establecer la conexión con la base de datos
    db = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()

    # Ejecutar la consulta para obtener los estados ordenados por su id
    cursor.execute("SELECT id, name FROM states ORDER BY id ASC")

    # Mostrar los resultados en el formato especificado
    for row in cursor.fetchall():
        print(row)

    # Cerrar la conexión
    cursor.close()
    db.close()

if __name__ == "__main__":
    # Verificar que se proporcionaron los 3 argumentos requeridos
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Llamar a la función para listar los estados
    list_states(username, password, database)
