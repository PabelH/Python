import sqlite3

db_connection = sqlite3.connect('ex1.db')
db_cursor = db_connection.cursor()

db_cursor.execute("CREATE TABLE Students(Id INT, Name TEXT, Lastname TEXT)")

db_cursor.execute("INSERT INTO Students VALUES(1,'Bob', 'Esponja')")
db_cursor.execute("INSERT INTO Students VALUES(2,'Patricio', 'Estrella')")
db_cursor.execute("INSERT INTO Students VALUES(3,'Calamardo', 'Tentaculos')")
db_cursor.execute("INSERT INTO Students VALUES(4,'Arenita', 'Mejilla')")
db_cursor.execute("INSERT INTO Students VALUES(5,'Gumball', 'Watterson')")
db_cursor.execute("INSERT INTO Students VALUES(6,'Darwin', 'Watterson')")
db_cursor.execute("INSERT INTO Students VALUES(7,'Tobías', 'Wilson')")
db_cursor.execute("INSERT INTO Students VALUES(8,'Banana', 'Joe')")

db_connection.commit()

db_cursor.execute("SELECT * FROM Students WHERE Name = 'Darwin'")

filas = db_cursor.fetchall()

print(filas)

db_connection.close()