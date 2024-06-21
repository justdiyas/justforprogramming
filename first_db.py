import sqlite3
from employee import Employee, Car

connection = sqlite3.connect('employee.db')
cursor = connection.cursor()

def create_table():
    cursor.execute("""CREATE TABLE cars
                (car_id INTEGER NOT NULL PRIMARY KEY,
                make VARCHAR(50) NOT NULL,
                model VARCHAR(50) NOT NULL);""")

    cursor.execute("""CREATE TABLE employees
        (id INTEGER NOT NULL PRIMARY KEY,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        profession VARCHAR(70) NOT NULL,
        pay INTEGER NOT NULL,
        car_id INTEGER,
        FOREIGN KEY (car_id) REFERENCES car(car_id));""")


def insert_emp(emp):
    with connection:
        cursor.execute("INSERT INTO employees VALUES (:id, :first_name, :last_name, :profession, :pay, :car_id);",
               {'id': emp.id, 'first_name': emp.first, 'last_name': emp.last, 'profession': emp.profession, 'pay': emp.pay, 'car_id': emp.car_id})

def insert_car(car):
    with connection:
        cursor.execute("INSERT INTO cars VALUES (:car_id, :make, :model);",
               {'car_id': car.car_id, 'make': car.make, 'model': car.model})


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

def drop_table(table):
    cursor.execute(f"DROP TABLE {table}")

# emp_5 = Employee(1, 'Abay', 'Kerimov', 'Go Developer', 800000, None)
# emp_6 = Employee(2, 'Gulmira', 'Sarsenova', 'Nurse', 300000, None)
#
# insert_emp(emp_5)
# insert_emp(emp_6)
# create_table()
# drop_table('employees')
# drop_table('cars')
car_1 = Car(1, 'Toyota', 'Camry 10')
car_2 = Car(2, 'Nissan', 'Premiera')
car_3 = Car(3, 'Mitsubishi', 'Galant')
insert_car(car_1)
insert_car(car_2)
insert_car(car_3)
get_all_from_table('employees')
get_all_from_table('cars')

connection.close()
