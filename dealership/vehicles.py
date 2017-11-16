class Vehicle(object):
    SALES_MULTIPLIER = None
    PURCHASE_MILEAGE_MULITPLIER = None
    INTEREST_RATE = None
    LEASE_MULTIPLIER = None
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.base_price = base_price
        self.miles = miles
        self.year = year
        
    def sale_price(self):
        return self.SALES_MULTIPLIER * self.base_price
    def purchase_price(self):
        return self.sale_price() - self.PURCHASE_MILEAGE_MULITPLIER * self.miles
    

class Car(Vehicle):
    SALES_MULTIPLIER = 1.2
    PURCHASE_MILEAGE_MULITPLIER = .004
    INTEREST_RATE = 1.07
    LEASE_MULTIPLIER = 1.2
    
class Motorcycle(Vehicle):
    SALES_MULTIPLIER = 1.1
    PURCHASE_MILEAGE_MULITPLIER = .009
    INTEREST_RATE = 1.03
    LEASE_MULTIPLIER = 1
    
class Truck(Vehicle):
    SALES_MULTIPLIER = 1.6
    PURCHASE_MILEAGE_MULITPLIER = .02
    INTEREST_RATE = 1.11
    LEASE_MULTIPLIER = 1.7
