LOCATIONS = [
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
]

def get_all_locations():
    return LOCATIONS

def get_single_location(id):
    requested_location = None

    for location in LOCATIONS:
        if location["id"] == id:
            requested_location = location

    return requested_location