class Vehicle(object):
    SALE_MULTIPLIER = 1
    PURCHASE_MULTIPLIER = 0
    LEASE_MULTIPLIER = 1
    
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles
    
    def sale_price(self):
        return self.base_price * self.SALE_MULTIPLIER

    def purchase_price(self):
        return self.sale_price() - (self.PURCHASE_MULTIPLIER * self.miles)

    def lease_multiplier(self,length_in_months):
        return (self.sale_price() * self.LEASE_MULTIPLIER ) / length_in_months
    
class Car(Vehicle):
    SALE_MULTIPLIER = 1.2
    PURCHASE_MULTIPLIER = 0.004
    INTEREST_RATE = 1.07
    LEASE_MULTIPLIER = 1.2

class Motorcycle(Vehicle):
    SALE_MULTIPLIER = 1.1
    PURCHASE_MULTIPLIER = 0.009
    INTEREST_RATE = 1.03
    LEASE_MULTIPLIER = 1


class Truck(Vehicle):
    SALE_MULTIPLIER = 1.6
    PURCHASE_MULTIPLIER = 0.02
    INTEREST_RATE = 1.11
    LEASE_MULTIPLIER = 1.7
