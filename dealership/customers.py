class Person(object):
    def __init__(self, first_name, last_name, email):
        # Define Person instance variables
        self.first_name = first_name
        self.last_name = last_name
        self.email = email


class Customer(Person):
    # Customer can buy or lease.
    def is_employee(self):
        return False


class Employee(Person):
    # Employee can buy or lease. Gets discount.
    def is_employee(self):
        return True