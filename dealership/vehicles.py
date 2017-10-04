class Vehicle(object):

    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles

    def sale_price(self):
        return self.base_price * self.SALE_MULTIPLIER

    def purchase_price(self):
        return self.sale_price() - (self.PURCHASE_MULTIPLIER * self.miles)


class Car(Vehicle):
    INTEREST_RATE = 1.07
    SALE_MULTIPLIER = 1.2
    PURCHASE_MULTIPLIER = 0.004
    LEASE_FACTOR = 1.2


class Motorcycle(Vehicle):
    INTEREST_RATE = 1.03
    SALE_MULTIPLIER = 1.1
    PURCHASE_MULTIPLIER = 0.009
    LEASE_FACTOR = 1


class Truck(Vehicle):
    INTEREST_RATE = 1.11
    SALE_MULTIPLIER = 1.6
    PURCHASE_MULTIPLIER = 0.02
    LEASE_FACTOR = 1.7
