class Vehicle(object):

    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles

    def sale_price(self):
        return self.base_price * self.sale_multiplier

    def purchase_price(self):
        return self.sale_price() - (self.purchase_multiplier * self.miles)


class Car(Vehicle):
    # no need to define __init__ here since Car will inherit all attributes of Vehicle
    # while introducing its own (constant) attributes

    # we call __init__ on the parent class here if we want to extend the __init__ in the parent class. That is, if we wanted Car to have an additional attribute (say presence of a sunroof) beyond maker, model, year, base_price, and miles.
    sale_multiplier = 1.2
    purchase_multiplier = 0.004


class Motorcycle(Vehicle):

    sale_multiplier = 1.1
    purchase_multiplier = 0.009


class Truck(Vehicle):

    sale_multiplier = 1.6
    purchase_multiplier = 0.02
