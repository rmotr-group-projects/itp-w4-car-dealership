class Vehicle(object):
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles
    
    S = None # sale multiplier
    P = None # purchase multiplier
    I = None # interest rate
    L = None # lease multiplier

    def sale_price(self):
        return self.base_price * self.S
        
    def purchase_price(self):
        return self.sale_price() - (self.P * self.miles)
    

class Car(Vehicle):
    S, P, I, L  = 1.2, 0.004, 1.07, 1.2


class Motorcycle(Vehicle):
    S, P, I, L = 1.1, 0.009, 1.03, 1


class Truck(Vehicle):
    S, P, I, L = 1.6, 0.02, 1.11, 1.7
