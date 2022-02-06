from conection_factory import ConnectionFactory

connection = ConnectionFactory().get_connection()

cursor = connection.cursor()
cursor.execute("Select * from cursos")

for linha in cursor:
    print(linha)

connection.close()
