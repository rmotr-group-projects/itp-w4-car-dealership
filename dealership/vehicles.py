class Vehicle(object):
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles
    
    def sale_price(self):
        return self.base_price * self.sale_multipliers
    
    def purchase_price(self):
        return self.sale_price() - (self.purchase_multipliers * self.miles)
        
        
class Car(Vehicle):
    sale_multipliers = 1.2
    purchase_multipliers = 0.004

class Motorcycle(Vehicle):
    sale_multipliers = 1.1
    purchase_multipliers = 0.009

class Truck(Vehicle):
    sale_multipliers = 1.6
    purchase_multipliers = 0.02

