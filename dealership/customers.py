class Person(object):
    '''Represents a person making a purchase at the car dealership.'''
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        
    def is_employee(self):
        raise NotImplementedError


class Customer(Person):
    '''Represents a typical customer.'''
    def is_employee(self):
        return False
        

class Employee(Person):
    '''Represents a customer who is also an employee.'''
    def is_employee(self):
        return True
