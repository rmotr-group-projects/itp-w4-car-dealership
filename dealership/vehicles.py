class Vehicle(object):
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles
        
    def sale_price(self):
        return self.S * self.base_price
        
    def purchase_price(self):
        return self.sale_price() - self.P * self.miles

class Car(Vehicle):
    S = 1.2
    P = 0.004
    I = 1.07
    M = 1.2
        



class Motorcycle(Vehicle):
    S = 1.1
    P = 0.009
    I = 1.03
    M = 1


class Truck(Vehicle):
    S = 1.6
    P = 0.02
    I = 1.11
    M = 1.7
