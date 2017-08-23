class Person(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

class Customer(Person):
    @classmethod
    def is_employee(cls):
        return False
    
class Employee(Person):
    @classmethod
    def is_employee(cls):
        return True