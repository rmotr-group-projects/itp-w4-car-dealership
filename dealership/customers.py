class Person(object):
    # Put discount in 
    discount = 0
    
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def is_employee(self):
        raise NotImplementedError()
    
# Put discounts here because they will be static for every instance of these classes aka Class Attributes 
class Customer(Person):
    def is_employee(self):
        return False
    

class Employee(Person):
    discount = .1
    
    def is_employee(self):
        return True