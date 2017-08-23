class Vehicle(object):
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles
    
class Car(Vehicle):
    sale_mutiplier = 1.2
    purchase_multiplier = 0.004
    I = 1.07
    lease_mutiplier_unit = 1.2
    
    def __int__(self, maker, model, year, base_price, miles):
        Vehicle.__init__(self, maker, model, year, base_price, miles)
    
    def sale_price(self):
        sale_price_for_vehicle = self.base_price * Car.sale_mutiplier
        return sale_price_for_vehicle
    
    def purchase_price(self):
        purchase_price_for_vehicle = self.sale_price() - (Car.purchase_multiplier * self.miles)
        return purchase_price_for_vehicle

class Motorcycle(Vehicle):
    sale_mutiplier = 1.1
    purchase_multiplier = 0.009
    I = 1.03
    lease_mutiplier_unit = 1
    
    def __int__(self, maker, model, year, base_price, miles):
        Vehicle.__init__(self, maker, model, year, base_price, miles)
        
    
    def sale_price(self):
        sale_price_for_vehicle = self.base_price * Motorcycle.sale_mutiplier
        return sale_price_for_vehicle
    
    def purchase_price(self):
        purchase_price_for_vehicle = self.sale_price() - (Motorcycle.purchase_multiplier * self.miles)
        return purchase_price_for_vehicle

class Truck(Vehicle):
    sale_mutiplier = 1.6
    purchase_multiplier = 0.02
    I = 1.11
    lease_mutiplier_unit = 1.7
    
    def __int__(self, maker, model, year, base_price, miles):
        Vehicle.__init__(self, maker, model, year, base_price, miles)
        
    
    def sale_price(self):
        sale_price_for_vehicle = self.base_price * Truck.sale_mutiplier
        return sale_price_for_vehicle
    
    def purchase_price(self):
        purchase_price_for_vehicle = self.sale_price() - (Truck.purchase_multiplier * self.miles)
        return purchase_price_for_vehicle
    
    
    
