class Vehicle(object):
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles


class Car(Vehicle):
    # Define purchase multipliers
    def __init__(self, maker, model, year, base_price, miles):
        # Inherit vehicle attributes
        super(Car, self).__init__(maker, model, year, base_price, miles)
    
    sale_multiplier = 1.2
    lease_multiplier = 1.2
    
    def sale_price(self):
        return self.base_price * self.sale_multiplier
        
    def purchase_price(self):
        p = 0.004
        return self.sale_price() - (p * self.miles)
    
    def interest_rate(self):
        return 1.07


class Motorcycle(Vehicle):
    def __init__(self, maker, model, year, base_price, miles):
        # Inherit vehicle attributes
        super(Motorcycle, self).__init__(maker, model, year, base_price, miles)
        
    sale_multiplier = 1.1
    lease_multiplier = 1
        
    def sale_price(self):
        return self.base_price * self.sale_multiplier
        
    def purchase_price(self):
        p = 0.009
        return self.sale_price() - (p * self.miles)
    
    def interest_rate(self):
        return 1.03

class Truck(Vehicle):
    def __init__(self, maker, model, year, base_price, miles):
        # Inherit vehicle attributes
        super(Truck, self).__init__(maker, model, year, base_price, miles)
        
    sale_multiplier = 1.6
    lease_multiplier = 1.7
        
    def sale_price(self):
        return self.base_price * self.sale_multiplier
        
    def purchase_price(self):
        p = 0.02
        return self.sale_price() - (p * self.miles)
        
    def interest_rate(self):
        return 1.11