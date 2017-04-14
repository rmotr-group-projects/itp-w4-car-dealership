class Person(object):
    def __init__(self, first_name, last_name, email):
       self.first_name = first_name
       self.last_name = last_name
       self.email = email
        
# PYTHONPATH=. py.test -s tests -k test_customers 

class Customer(Person):
    def is_employee(self):
        return False


class Employee(Person):
    def is_employee(self):
        return True


# import unittest

# from dealership.customers import Customer, Employee


# class CustomerTestCase(unittest.TestCase):
#     def test_if_are_employee(self):
#         c = Customer('John', 'Doe', 'john@example.com')
#         self.assertEqual(c.first_name, 'John')
#         self.assertEqual(c.last_name, 'Doe')
#         self.assertEqual(c.email, 'john@example.com')
#         self.assertFalse(c.is_employee())

#         e = Employee('Jane', 'Doe', 'jane@example.com')
#         self.assertEqual(e.first_name, 'Jane')
#         self.assertEqual(e.last_name, 'Doe')
#         self.assertEqual(e.email, 'jane@example.com')
#         self.assertTrue(e.is_employee())

