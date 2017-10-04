class Vehicle(object):
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles

    def sale_price(self):
        return self.base_price * self.SALE_MULT
    
    def purchase_price(self):
        return (self.sale_price()) - (self.miles * self.PURCHASE_MULT)
        
        
class Car(Vehicle):
    SALE_MULT = 1.2
    PURCHASE_MULT = 0.004
    INTEREST_RATE = 1.07
    LEASE_MULT = 1.2
    
class Motorcycle(Vehicle):
    SALE_MULT = 1.1
    PURCHASE_MULT = 0.009
    INTEREST_RATE = 1.03
    LEASE_MULT = 1

class Truck(Vehicle):
    SALE_MULT = 1.6
    PURCHASE_MULT = 0.02
    INTEREST_RATE = 1.11
    LEASE_MULT = 1.7