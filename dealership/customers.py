class Person(object):
    dummy = False
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
    def is_employee(self):
        return self.dummy
        


class Customer(Person):
    dummy = False
        


class Employee(Person):
    dummy = True

"""
class Animal(object):
    def __init__(self, what_i_say_when_talk):
        self.what_i_say_when_talk = what_i_say_when_talk
    def talk(self):
        return self.what_i_say_when_talk


class Cat(Animal):
    pass
        
class Dog(Animal):
    pass
        
class Human(Animal):
    pass
            """