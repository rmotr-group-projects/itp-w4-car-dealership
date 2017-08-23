class Vehicle(object):
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles

    def sale_price(self):
        return self.base_price * self.sale_multiplier()
    
    def purchase_price(self):
        return (self.sale_price()) - (self.miles * self.purchase_multiplier())
        
 
 
class Car(Vehicle):
    def sale_multiplier(self):
        return 1.2
    
    def purchase_multiplier(self):
        return 0.004

class Motorcycle(Vehicle):
    def sale_multiplier(self):
        return 1.1
    
    def purchase_multiplier(self):
        return 0.009

class Truck(Vehicle):
    def sale_multiplier(self):
        return 1.6
    
    def purchase_multiplier(self):
        return 0.02