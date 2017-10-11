class Vehicle(object):
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles
    
    def sale_price(self):
        return self.base_price * self.sale_price_multiplier
    
    def purchase_price(self):
        return self.sale_price() - (self.purchase_price_multiplier * self.miles)
        
class Car(Vehicle):
    def __init__(self, maker, model, year, base_price, miles):
        super(Car, self).__init__(maker, model, year, base_price, miles)
        self.sale_price_multiplier = 1.2
        self.purchase_price_multiplier = .004
        self.interest = 1.07
        self.lease_mulitiplier = 1.2

class Motorcycle(Vehicle):
    def __init__(self, maker, model, year, base_price, miles):
        super(Motorcycle, self).__init__(maker, model, year, base_price, miles)
        self.sale_price_multiplier = 1.1
        self.purchase_price_multiplier = .009
        self.interest = 1.03
        self.lease_mulitiplier = 1


class Truck(Vehicle):
    def __init__(self, maker, model, year, base_price, miles):
        super(Truck, self).__init__(maker, model, year, base_price, miles)
        self.sale_price_multiplier = 1.6
        self.purchase_price_multiplier = .02
        self.interest = 1.11
        self.lease_mulitiplier = 1.7