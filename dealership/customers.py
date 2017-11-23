class Person(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        #print('test')


class Customer(Person):
    def is_employee(self):
        return False
        


class Employee(Person):
    def is_employee(self):
        return True
        


# def test_customer_is_not_employee():
#     c = Customer('John', 'Doe', 'john@example.com')
#     assert c.first_name == 'John'
#     assert c.last_name == 'Doe'
#     assert c.email == 'john@example.com'
#     assert c.is_employee() is False
    


# def test_customer_is_employee():
#     e = Employee('Jane', 'Doe', 'jane@example.com')
#     assert e.first_name == 'Jane'
#     assert e.last_name == 'Doe'
#     assert e.email == 'jane@example.com'
#     assert e.is_employee() is True


# test_customer_is_not_employee()
# test_customer_is_employee()

#print('Hello World')

