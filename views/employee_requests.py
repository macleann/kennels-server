import sqlite3
import json
from models import Employee, Location, Animal

def get_all_employees():
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address,
            e.location_id,
            l.name location_name,
            l.address location_address
        FROM Employee e
        JOIN Location l
            ON l.id = e.location_id
        """)

        employees = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['id'], row['name'],
                                row['address'], row['location_id'])

            location = Location(row['id'], row['location_name'], row['location_address'])

            employee.location = location.__dict__

            employees.append(employee.__dict__)

    return employees

def get_single_employee(id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address,
            e.location_id,
            ea.employee_id,
            ea.animal_id,
            a.id animal_id,
            a.name animal_name,
            a.status,
            a.breed,
            a.customer_id
        FROM Employee e
        JOIN EmployeeAnimal ea ON ea.employee_id = e.id
        JOIN Animal a ON a.id = ea.animal_id
        WHERE e.id = ?
        """, ( id, ))

        dataset = db_cursor.fetchall()
        animals = []
        employee = None

        for row in dataset:
            if employee is None:
                employee = Employee(row['id'], row['name'],
                            row['address'], row['location_id'])
            else:
                animal = Animal(row['animal_id'], row['animal_name'], row['status'],
                                row['breed'], row['customer_id'], row['location_id'])
                animals.append(animal.__dict__)
        employee.animals = animals

        return employee.__dict__

def get_employees_by_location(location_id):

    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address,
            e.location_id
        FROM Employee e
        WHERE e.location_id = ?
        """, ( location_id, ))

        employees = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['id'], row['name'], row['address'], row['location_id'])
            employees.append(employee.__dict__)

    return employees

def create_employee(new_employee):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Employee
            ( name, address, location_id )
        VALUES
            ( ?, ?, ?);
        """, (new_employee['name'], new_employee['address'],
              new_employee['location_id'], ))

        id = db_cursor.lastrowid

        new_employee['id'] = id


    return new_employee
  
def delete_employee(id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM employee
        WHERE id = ?
        """, (id, ))
        
def update_employee(id, new_employee):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Employee
            SET
                name = ?,
                address = ?,
                location_id = ?
        WHERE id = ?
        """, (new_employee['name'], new_employee['address'],
              new_employee['location_id'], id, ))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True
