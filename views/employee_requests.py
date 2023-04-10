EMPLOYEES = [
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
]

def get_all_employees():
    return EMPLOYEES

def get_single_employee(id):
    requested_employee = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee