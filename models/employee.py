class Employee():
    def __init__(self, id, name, address, location_id):
        self.id = id
        self.name = name
        self.address = address
        self.location_id = location_id
        self.animals = None

class EmployeeAnimal():
    def __init__(self, animals):
        self.animals = animals
