import sqlite3

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








# class Employee:
#     def __init__(self, first, last, profession, pay):
#         self.first = first
#         self.last = last
#         self.profession = profession
#         self.pay = pay
#
#     @property
#     def email(self):
#         return f'{self.first}.{self.last}@email.com'.lower()
#
#     @property
#     def fullname(self):
#         return f'{self.first} {self.last}'
#
#     def __repr__(self):
#         return f'First name: {self.first} \nLast name: {self.last} \nProfession: {self.profession} \nPay rate: {self.pay}'
#
#
# emp = Employee('Diyas', 'Iyemberdiyev', 'Python Developer', 900000)
# print(emp)