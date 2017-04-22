class Person(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def is_employee(self):
       return self.EMPLOYEE_STATUS


class Customer(Person):
    EMPLOYEE_STATUS = False


class Employee(Person):
    EMPLOYEE_STATUS = True
    