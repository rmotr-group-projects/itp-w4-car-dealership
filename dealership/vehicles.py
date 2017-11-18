class Vehicle(object):
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles
    
    #Placeholders for the constants    
    SALE_MULTIPLIER = None
    PURCHASE_MULTIPLIER = None
    INTEREST_RATE = None
    LEASE_RATE = None
    
    def sale_price(self):
        return self.base_price * self.SALE_MULTIPLIER
        
    def purchase_price(self):
        return self.sale_price() - (self.PURCHASE_MULTIPLIER * self.miles)

class Car(Vehicle):
    SALE_MULTIPLIER = 1.2
    PURCHASE_MULTIPLIER = 0.004
    INTEREST_RATE = 1.07
    LEASE_RATE = 1.2

class Motorcycle(Vehicle):
    SALE_MULTIPLIER = 1.1
    PURCHASE_MULTIPLIER = 0.009
    INTEREST_RATE = 1.03
    LEASE_RATE = 1


class Truck(Vehicle):
    SALE_MULTIPLIER = 1.6
    PURCHASE_MULTIPLIER = 0.02
    INTEREST_RATE = 1.11
    LEASE_RATE = 1.7
