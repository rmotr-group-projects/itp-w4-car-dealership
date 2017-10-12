class Person(object):
    
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
    
    # Made this a classmethod so both Customers and Employees could use it as well as to check the cls
    # Don't know if this was the right way to do it. might be able to use self.__class__.__name__
    @classmethod
    def is_employee(cls):
        return cls == Employee

# Put discounts here because they will be static for every instance of these classes aka Class Attributes 
class Customer(Person):
    discount = 0

class Employee(Person):
    discount = .1
