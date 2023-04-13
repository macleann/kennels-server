DATABASE = {
    "ANIMALS" : [
    {
        "id": 1,
        "name": "Snickers",
        "species": "Dog",
        "locationId": 1,
        "customerId": 4,
        "status": "Admitted"
    },
    {
        "id": 2,
        "name": "Roman",
        "species": "Dog",
        "locationId": 1,
        "customerId": 2,
        "status": "Admitted"
    },
    {
        "id": 3,
        "name": "Blue",
        "species": "Cat",
        "locationId": 2,
        "customerId": 1,
        "status": "Admitted"
    }
],
    "LOCATIONS" : [
    {
      "id": 1,
      "name": "Nashville North",
      "address": "8422 Johnson Pike"
    },
    {
      "id": 2,
      "name": "Nashville South",
      "address": "209 Emory Drive"
    },
    {
      "name": "Nashville East",
      "address": " 1901 Gallatin Pike",
      "id": 3
    }
],
    "EMPLOYEES" : [
    {
      "id": 1,
      "name": "James Baxter"
    },
    {
      "id": 2,
      "name": "Raquel Roberts"
    },
    {
      "name": "Johnny James",
      "id": 3
    }
],
    "CUSTOMERS" : [
    {
        "id": 1,
        "name": "Ryan Tanay"
    },
    {
        "id": 2,
        "name": "Zoila Cummerata"
    },
    {
        "id": 3,
        "name": "Tristian Nikolaus"
    }
]
 }


def all(resource):
    """For GET requests to collection"""
    return DATABASE[resource.upper()]


def retrieve(resource, id):
    """For GET requests to a single resource"""
    requested_resource = None
    
    for single_resource in DATABASE[resource.upper()]:
        if single_resource["id"] == id:
            requested_resource = single_resource
            return requested_resource


def create(resource, new_resource):
    """For POST requests to a collection"""
    max_id = DATABASE[resource.upper()][-1]["id"]
    new_id = max_id + 1
    new_resource["id"] = new_id
    DATABASE[resource.upper()].append(new_resource)
    return new_resource

def update(resource, id, new_resource):
    """For PUT requests to a single resource"""
    for index, single_resource in enumerate(DATABASE[resource.upper()]):
        if single_resource["id"] == id:
            DATABASE[resource.upper()][index] = new_resource


def delete(resource, id):
    """For DELETE requests to a single resource"""
    resource_index = -1

    for index, single_resource in enumerate(DATABASE[resource.upper()]):
        if single_resource["id"] == id:
            resource_index = index

    if resource_index >= 0:
        DATABASE[resource.upper()].pop(resource_index)
