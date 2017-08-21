class Vehicle(object):
    SALE_MULTI = 1
    PURCHASE_MULTI = 1
    
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles
        
    def sale_price(self):
        return self.base_price * self.SALE_MULTI
        
    def purchase_price(self):
        return self.sale_price() - (self.PURCHASE_MULTI * self.miles)

class Car(Vehicle):
    
    SALE_MULTI = 1.2
    PURCHASE_MULTI = 0.004
    INTEREST = 1.07
    LEASE_MULTI = 1.2

class Motorcycle(Vehicle):
    
    SALE_MULTI = 1.1
    PURCHASE_MULTI = 0.009
    INTEREST = 1.03
    LEASE_MULTI = 1

class Truck(Vehicle):
    
    SALE_MULTI = 1.6
    PURCHASE_MULTI = 0.02
    INTEREST = 1.11
    LEASE_MULTI = 1.7