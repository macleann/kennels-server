class Location():
    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address
        self.animals = None

class LocationAnimal():
    def __init__(self, animals):
        self.animals = animals