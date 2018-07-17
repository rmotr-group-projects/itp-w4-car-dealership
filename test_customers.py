from dealership.customers import Customer, Employee

"""
Checks to see if the Customer and Employee object are created correctly.

For Customer object, then `is_employee` method should return false
For Employee object, then `is_employee` method should return true
"""
def test_if_are_employee():
    c = Customer('John', 'Doe', 'john@example.com')
    assert c.first_name == 'John'
    assert c.last_name == 'Doe'
    assert c.email == 'john@example.com'
    assert not c.is_employee()

    e = Employee('Jane', 'Doe', 'jane@example.com')
    assert e.first_name == 'Jane'
    assert e.last_name == 'Doe'
    assert e.email == 'jane@example.com'
    assert e.is_employee()
