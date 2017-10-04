class Person(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

class Customer(Person):
    CUSTOMER_DISC = 0.0
    def is_employee(self):
        return False


class Employee(Person):
    CUSTOMER_DISC = 0.1
    def is_employee(self):
        return True
