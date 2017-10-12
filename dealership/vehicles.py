class Vehicle(object):
    purchase_multiplier = None
    sale_multiplier = None

    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles
    
    def sale_price(self):
        return self.base_price * self.purchase_multiplier
    
    def purchase_price(self):
        return self.sale_price() - (self.sale_multiplier * self.miles)

class Car(Vehicle):
    purchase_multiplier = 1.2
    sale_multiplier = .004

class Motorcycle(Vehicle):
    purchase_multiplier = 1.1
    sale_multiplier = .009

        
class Truck(Vehicle):
    purchase_multiplier = 1.6
    sale_multiplier = .02

