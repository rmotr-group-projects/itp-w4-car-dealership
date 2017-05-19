class Vehicle(object):
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles


class Car(Vehicle):
    def sale_price(self):
        # Take base price, multiply by sale modifier
        return self.base_price * 1.2
        
    def purchase_price(self):
        # Do sale price math, then calculate purchase price
        return (self.base_price * 1.2) - (0.004 * self.miles)
    

class Motorcycle(Vehicle):
    def sale_price(self):
        # Take base price, multiply by sale modifier
        return self.base_price * 1.1
        
    def purchase_price(self):
        # Do sale price math, then calculate purchase price
        return (self.base_price * 1.1) - (0.009 * self.miles)
    


class Truck(Vehicle):
    def sale_price(self):
        # Take base price, multiply by sale modifier
        return self.base_price * 1.6
        
    def purchase_price(self):
        # Do sale price math, then calculate purchase price
        return (self.base_price * 1.6) - (0.02 * self.miles)
    

