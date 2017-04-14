class Person(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        
    def is_employee(self):
        if isinstance(self, Employee):
            return True
        return False

class Customer(Person):
    pass

class Employee(Person):
    pass

