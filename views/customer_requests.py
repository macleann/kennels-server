CUSTOMERS = [
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

def get_all_customers():
    return CUSTOMERS

def get_single_customer(id):
    requested_customer = None

    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer