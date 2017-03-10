class Vehicle(object):
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles
    
class Car(Vehicle):
    S = 1.2
    P =.004
    I = 1.07
    M = 1.2
    
    def sale_price(self):
        return self.base_price * self.S
        
    def purchase_price(self):
        return self.sale_price() - (self.P * self.miles)

class Motorcycle(Vehicle):
    S = 1.1
    P =.009
    I = 1.03
    M = 1
    
    def sale_price(self):
        return self.base_price * self.S
        
    def purchase_price(self):
        return self.sale_price() - (self.P * self.miles)


class Truck(Vehicle):
    S = 1.6
    P =.02
    I = 1.11
    M = 1.7
    
    def sale_price(self):
        return self.base_price * self.S
        
    def purchase_price(self):
        return self.sale_price() - (self.P * self.miles)