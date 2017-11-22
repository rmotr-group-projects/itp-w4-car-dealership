class Vehicle(object):
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker 
        self.model = model
        self.year = year 
        self.base_price = base_price
        self.miles = miles 

# Sale multipliers
# Car: 1.2
# Motorcycle: 1.1
# Truck: 1.6

# Purchase multipliers
# Car: 0.004
# Motorcycle: 0.009
# Truck: 0.02
        
# add dict to hold sale price and purchase price 
class Car(Vehicle):
    sale_multiplier = 1.2
    purchase_multiplier = 0.004
    
    def sale_price(self):
        return self.base_price * Car.sale_multiplier
        
    def purchase_price(self):
        return self.sale_price() - self.miles*Car.purchase_multiplier
        

class Motorcycle(Vehicle):
    sale_multiplier = 1.1
    purchase_multiplier = 0.009
    
    def sale_price(self):
        return self.base_price* Motorcycle.sale_multiplier
        
    def purchase_price(self):
        return self.sale_price() - self.miles*Motorcycle.purchase_multiplier
        
class Truck(Vehicle):
    sale_multiplier = 1.6
    purchase_multiplier = 0.02
    
    def sale_price(self):
        return self.base_price* Truck.sale_multiplier
        
    def purchase_price(self):
        return self.sale_price() - self.miles*Truck.purchase_multiplier




