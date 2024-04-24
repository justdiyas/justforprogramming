import sqlite3
from employee import Employee

connection = sqlite3.connect('employee.db')
cursor = connection.cursor()

# cursor.execute("""CREATE TABLE employees
#     (first_name VARCHAR(50),
#     last_name VARCHAR(50),
#     profession VARCHAR(70),
#     pay INTEGER);""")

def insert_emp(emp):
    with connection:
        cursor.execute("INSERT INTO employees VALUES (:first_name, :last_name, :profession, :pay);",
               {'first_name': emp.first, 'last_name': emp.last, 'profession': emp.profession, 'pay': emp.pay})


def get_emp_by_name(first_name):
    cursor.execute("SELECT * FROM employees WHERE first_name=:first_name;", {'first_name': first_name})
    return cursor.fetchall()


def update_pay(emp, pay):
    with connection:
        cursor.execute("""UPDATE employees SET pay=:pay 
                        WHERE first_name=:first_name AND last_name=:last_name""",
                        {'first_name': emp.first, 'last_name': emp.last, 'pay': pay})


def remove_emp(emp):
    with connection:
        cursor.execute("""DELETE FROM employees 
                        WHERE first_name=:first_name AND last_name=:last_name""",
                       {'first_name': emp.first, 'last_name': emp.last})


def get_all_from_table(table):
    cursor.execute(f"SELECT * FROM {table};")
    print(cursor.fetchall())


emp_5 = Employee('Abay', 'Kerimov', 'Go Developer', 800000)
emp_6 = Employee('Gulmira', 'Sarsenova', 'Nurse', 300000)

# insert_emp(emp_5)
# insert_emp(emp_6)
# get_all_from_table('employees')

connection.close()
