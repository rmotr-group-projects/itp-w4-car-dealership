class Vehicle(object):
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles
    
    def sale_price(self):
        return self.base_price * self.__class__.Sale_multiplier
    
    def purchase_price(self):
        return self.sale_price() - (self.__class__.Purchase_multiplier * self.miles)
        
class Car(Vehicle):
    Sale_multiplier = 1.2
    Purchase_multiplier = 0.004
    interest_rate = 1.07
    lease_multiplier = 1.2
        

class Motorcycle(Vehicle):
    Sale_multiplier = 1.1
    Purchase_multiplier = 0.009
    interest_rate = 1.03
    lease_multiplier = 1

class Truck(Vehicle):
    Sale_multiplier = 1.6
    Purchase_multiplier = 0.02
    interest_rate = 1.11
    lease_multiplier = 1.7