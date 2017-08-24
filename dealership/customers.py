class Person(object):
    DISCOUNT = 0

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.discount = Person.DISCOUNT

    def is_employee(self):
        return None


class Customer(Person):

    def is_employee(self):
        return False


class Employee(Person):
    DISCOUNT = 0.1

    def __init__(self, first_name, last_name, email):
        super(Employee, self).__init__(first_name, last_name, email)
        self.discount = Employee.DISCOUNT

    def is_employee(self):
        return True
