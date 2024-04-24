import sqlite3
from .employee import Employee

connection = sqlite3.connect('employee.db')
cursor = connection.cursor()

# cursor.execute("""CREATE TABLE employees
#     (first_name VARCHAR(50),
#     last_name VARCHAR(50),
#     profession VARCHAR,
#     pay INTEGER);
# """)

# cursor.execute("INSERT INTO employees VALUES ('Diyas', 'Iyemberdiyev', 'Python Developer', 700000);")

# cursor.execute("DELETE FROM employees WHERE last_name = 'Iyemberdiyev';")

cursor.execute("SELECT * FROM employees;")
print(cursor.fetchall())

connection.commit()
connection.close()
