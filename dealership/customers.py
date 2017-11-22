class Person(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email


class Customer(Person):
    def __init__(self, first_name, last_name, email):
        
        Person.__init__(self, first_name, last_name, email)
    
    def is_employee(self):
        return False
        raise NotImplementedError()

class Employee(Person):
    def __init__(self, first_name, last_name, email):
        Person.__init__(self, first_name, last_name, email)
    
    def is_employee(self):
        return True
        
    def is_customer(self):
        return False
