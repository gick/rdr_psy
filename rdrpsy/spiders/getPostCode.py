import mysql.connector as mariadb
mariadb_connection=mariadb.connect(user='python_user',password='1984', database='villes')
cursor=mariadb_connection.cursor()
cursor.execute("SELECT `ville_code_postal`, `ville_nom` FROM `villes_france_free` ORDER BY `ville_population_2012` DESC LIMIT 500")
cursor.fetchall