class Vehicle(object):
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model 
        self.year = year 
        self.base_price= base_price
        self.miles = miles


class Car(Vehicle):
    def __init__(self, maker, model, year, base_price, miles):
        Vehicle.__init__(self, maker, model, year, base_price, miles)
        self.multiplier = { 
            'sale': 1.2,
            'purchase': 0.004
        }
 

class Motorcycle(Vehicle):
    def __init__(self, maker, model, year, base_price, miles):
        Vehicle.__init__(self, maker, model, year, base_price, miles)
        self.multiplier = { 
            'sale': 1.1,
            'purchase': 0.009
        }


class Truck(Vehicle):
    def __init__(self, maker, model, year, base_price, miles):
        Vehicle.__init__(self, maker, model, year, base_price, miles)
        self.multiplier = { 
            'sale': 1.6,
            'purchase': 0.02
        }
