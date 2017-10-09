class Vehicle(object):
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model 
        self.year = year 
        self.base_price= base_price
        self.miles = miles


class Car(Vehicle):
    pass


class Motorcycle(Vehicle):
    pass


class Truck(Vehicle):
    pass
