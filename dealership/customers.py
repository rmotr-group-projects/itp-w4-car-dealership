class Person(object):
    def __init__(self, first_name, last_name, email):
        # Personal info/details
        self.first_name = first_name
        self.last_name = last_name
        self.email = email


class Customer(Person):
    # Not am employee, clearly
    def is_employee(self):
        return False


class Employee(Person):
    # Clearly an employee
    def is_employee(self):
        return True
