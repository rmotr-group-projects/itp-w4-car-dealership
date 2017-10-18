class Vehicle(object):
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles
        
    def sale_price(self):
        return self.base_price * self.purchase_multiplier
        
    def purchase_price(self):
        return self.sale_price() - (self.sale_multiplier * self.miles)    

class Car(Vehicle):
    interest = 1.07
    lease_multiplier = 1.2
    sale_multiplier = .004
    purchase_multiplier = 1.2


class Motorcycle(Vehicle):
    interest = 1.03
    lease_multiplier = 1
    sale_multiplier = .009
    purchase_multiplier = 1.1


class Truck(Vehicle):
    interest = 1.11
    lease_multiplier = 1.7
    sale_multiplier = .02
    purchase_multiplier = 1.6

