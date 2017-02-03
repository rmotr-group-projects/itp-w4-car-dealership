class Vehicle(object):
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles
        
    def sale_price(self):
        return self.base_price * self.SALE_RATE
        
    def purchase_price(self):
        return self.sale_price() - (self.PURCHASE_RATE * self.miles)
    

class Car(Vehicle):
    SALE_RATE = 1.2
    PURCHASE_RATE = 0.004  
    INTEREST_RATE = 1.07
    LEASE_RATE = 1.2


class Motorcycle(Vehicle):
    SALE_RATE = 1.1 
    PURCHASE_RATE = 0.009 
    INTEREST_RATE = 1.03
    LEASE_RATE = 1.0


class Truck(Vehicle):
    SALE_RATE = 1.6 
    PURCHASE_RATE = 0.02 
    INTEREST_RATE = 1.11
    LEASE_RATE = 1.7
