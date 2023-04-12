import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from views import get_all_animals, get_single_animal, create_animal, delete_animal, update_animal, get_all_locations, get_single_location, create_location, delete_location, update_location, get_all_employees, get_single_employee, create_employee, delete_employee, update_employee, get_all_customers, get_single_customer, create_customer, update_customer


# Here's a class. It inherits from another class.
# For now, think of a class as a container for functions that
# work together for a common purpose. In this case, that
# common purpose is to respond to HTTP requests from a client.
class HandleRequests(BaseHTTPRequestHandler):
    # This is a Docstring it should be at the beginning of all classes and functions
    # It gives a description of the class or function
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """

    # Here's a class function

    # Here's a method on the class that overrides the parent's method.
    # It handles any GET request.
    def do_GET(self):
        self._set_headers(200)
        response = {}  # Default response

        # Parse the URL and capture the tuple that is returned
        (resource, id) = self.parse_url(self.path)

        if resource == "animals":
            if id is not None:
                response = get_single_animal(id)
                if response is None:
                    self._set_headers(404)
                    response = "Animal not found"
            else:
                response = get_all_animals()
        elif resource == "locations":
            if id is not None:
                response = get_single_location(id)
                if response is None:
                    self._set_headers(404)
                    response = "Location not found"
            else:
                response = get_all_locations()
        elif resource == "employees":
            if id is not None:
                response = get_single_employee(id)
                if response is None:
                    self._set_headers(404)
                    response = "Employee not found"
            else:
                response = get_all_employees()
        elif resource == "customers":
            if id is not None:
                response = get_single_customer(id)
                if response is None:
                    self._set_headers(404)
                    response = "Customer not found"
            else:
                response = get_all_customers()
        else:
            response = []

        # Send a JSON formatted string as a response
        self.wfile.write(json.dumps(response).encode())


    # Here's a method on the class that overrides the parent's method.
    # It handles any POST request.
    def do_POST(self):
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        # Convert JSON string to a Python dictionary
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Initialize new resource
        new_resource = None
        post_keys = post_body.keys()
        check_keys = { "animals": ["name", "species", "locationId", "customerId", "status"],
                   "locations": ["name", "address"],
                   "employees": "name",
                   "customers": "name" }

        # Add a new resource to the list.
        if resource == "animals":
            # This first if statement iterates through the keys in check_keys and, if they exist in post_keys, adds them to the enclosing list
            # Once the iterations are complete, if the new list == check_keys["animals"], we can post the new animal
            if [key for key in check_keys["animals"] if key in post_body] == check_keys["animals"]:
                new_resource = create_animal(post_body)
            # Otherwise, set a 400 header response
            # Use the same logic to create a new list, but make it all keys NOT in post_body set to a new error_keys variable
            # Lastly, there's just some conditional logic for syntactically correct grammar
            else:
                self._set_headers(400)
                error_keys = [key for key in check_keys["animals"] if key not in post_body]
                if len(error_keys) > 2:
                    new_resource = f"message: {', '.join(error_keys)} are required"
                elif len(error_keys) > 1:
                    new_resource = f"message: {' and '.join(error_keys)} are required"
                else:
                    new_resource = f"message: {error_keys[0]} is required"
        elif resource == "locations":
            if [key for key in check_keys["locations"] if key in post_body] == check_keys["locations"]:
                new_resource = create_location(post_body)
            else:
                self._set_headers(400)
                error_keys = [key for key in check_keys["locations"] if key not in post_body]
                if len(error_keys) > 1:
                    new_resource = f"message: {' and '.join(error_keys)} are required"
                else:
                    new_resource = f"message: {error_keys[0]} is required"
        elif resource == "employees":
            if "name" in post_keys:
                new_resource = create_employee(post_body)
            else:
                new_resource = "message: name is required"
        elif resource == "customers":
            if "name" in post_keys:
                new_resource = create_customer(post_body)
            else:
                new_resource = "message: name is required"

        # Encode the new resource and send in response
        self.wfile.write(json.dumps(new_resource).encode())


    # A method that handles any PUT request.
    def do_PUT(self):
        self._set_headers(204)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Delete a single animal from the list
        if resource == "animals":
            update_animal(id, post_body)
        elif resource == "locations":
            update_location(id, post_body)
        elif resource == "employees":
            update_employee(id, post_body)
        elif resource == "customers":
            update_customer(id, post_body)

        # Encode the new animal and send in response
        self.wfile.write("".encode())
        
    def do_DELETE(self):
        # Set a 204 response code

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Delete a single animal from the list
        if resource == "animals":
            self._set_headers(204)
            delete_animal(id)
        elif resource == "locations":
            self._set_headers(204)
            delete_location(id)
        elif resource == "employees":
            self._set_headers(204)
            delete_employee(id)
        elif resource == "customers":
            self._set_headers(405)
            response = "Deleting customer requires contacting the company directly"
            self.wfile.write(json.dumps(response).encode())

        # Encode the new animal and send in response
        self.wfile.write("".encode())

    def _set_headers(self, status):
        # Notice this Docstring also includes information about the arguments passed to the function
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    # Another method! This supports requests with the OPTIONS verb.
    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def parse_url(self, path):
        # Just like splitting a string in JavaScript. If the
        # path is "/animals/1", the resulting list will
        # have "" at index 0, "animals" at index 1, and "1"
        # at index 2.
        path_params = path.split("/")
        resource = path_params[1]
        id = None

        # Try to get the item at index 2
        try:
            # Convert the string "1" to the integer 1
            # This is the new parseInt()
            id = int(path_params[2])
        except IndexError:
            pass  # No route parameter exists: /animals
        except ValueError:
            pass  # Request had trailing slash: /animals/

        return (resource, id)  # This is a tuple

# This function is not inside the class. It is the starting
# point of this application.


def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
