class Vehicle(object):
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles
    

class Car(Vehicle):
    
    INTEREST_RATE = 1.07
    
    def sale_price(self):
        return self.base_price * 1.2
    
    def purchase_price(self):
        return self.sale_price() - (0.004 * self.miles)
    
    def lease_multiplier(self, length_in_months):
        return self.sale_price() * 1.2 / length_in_months


class Motorcycle(Vehicle):
    
    INTEREST_RATE = 1.03
    
    def sale_price(self):
        return self.base_price * 1.1
    
    def purchase_price(self):
        return self.sale_price() - (0.009 * self.miles)
    
    def lease_multiplier(self, length_in_months):
        return self.sale_price() * 1 / length_in_months
        

class Truck(Vehicle):
    
    INTEREST_RATE = 1.11
    
    def sale_price(self):
        return self.base_price * 1.6
    
    def purchase_price(self):
        return self.sale_price() - (0.02 * self.miles)
    
    def lease_multiplier(self, length_in_months):
        return self.sale_price() * 1.7 / length_in_months
        
        
        
        
        
        
