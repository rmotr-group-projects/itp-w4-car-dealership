class Person(object):
    def __init__(self, first_name, last_name, email, discount=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = "{}@example.com".format(self.first_name).lower()
        self.discount = None

    def is_employee(self):
        return False


class Customer(Person):
    def __init__(self, first_name, last_name, email):
        super(Customer, self).__init__(first_name, last_name, email)


class Employee(Person):
    def __init__(self, first_name, last_name, email, discount=0.10):
        super(Employee, self).__init__(first_name, last_name, email)
        self.discount = discount

    def is_employee(self):
        return True
