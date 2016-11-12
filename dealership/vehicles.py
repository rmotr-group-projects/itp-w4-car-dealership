class Vehicle(object):
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles

    def sale_price(self):
        return self.base_price * self.sale_price_adjustment
        
    
    def purchase_price(self):
        return self.sale_price() - (self.purchase_price_adjustment * self.miles)
        
        

class Car(Vehicle):
    sale_price_adjustment = 1.2
    purchase_price_adjustment = 0.004
    
    def get_interest_rate(self):
        return 1.07
        
    def get_lease_multiplier(self, sale_price, length_in_months):
        return (sale_price() * 1.2 / length_in_months)

class Motorcycle(Vehicle):
    sale_price_adjustment = 1.1
    purchase_price_adjustment = 0.009
    
    def get_interest_rate(self):
        return 1.03
        
    def get_lease_multiplier(self, sale_price, length_in_months):
        return (sale_price() * 1 / length_in_months)   

class Truck(Vehicle):
    sale_price_adjustment = 1.6
    purchase_price_adjustment = 0.02
    
    def get_interest_rate(self):
        return 1.11
        
    def get_lease_multiplier(self, sale_price, length_in_months):
        return (sale_price() * 1.7 / length_in_months)

    
