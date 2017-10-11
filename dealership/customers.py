class Person(object):
    """Base class for people at a car dealership"""

    def __init__(self, first_name, last_name, email, discount=None):
        """Gather all necessary information for a customer"""

        self.first_name = first_name
        self.last_name = last_name
        self.email = "{}@example.com".format(self.first_name).lower()
        self.discount = None

    def is_employee(self):
        """Default customer should not be an employee"""

        return False


class Customer(Person):
    """Customers at the car dealership"""

    def __init__(self, first_name, last_name, email):
        """Customers inherit traits from Person class"""

        super(Customer, self).__init__(first_name, last_name, email)


class Employee(Person):
    """Employees at the car dealership"""

    def __init__(self, first_name, last_name, email, discount=0.10):
        """Employees inherit traits from the Person class"""

        super(Employee, self).__init__(first_name, last_name, email)
        self.discount = discount

    def is_employee(self):
        """Employees get special benefits, so we want to know who they are"""

        return True
