class Vehicle(object):
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model


class Car(Vehicle):
    pass


class Motorcycle(Vehicle):
    pass


class Truck(Vehicle):
    pass
