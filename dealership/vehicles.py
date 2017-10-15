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

    def sale_price(self):
        s = 1.2
        return self.base_price * s
        
    def purchase_price(self):
        p = 0.004
        return self.sale_price() - (p * self.miles)
    
    def interest_rate(self):
        return 1.07


class Motorcycle(Vehicle):
    def __init__(self, maker, model, year, base_price, miles):
        # Inherit vehicle attributes
        super(Motorcycle, self).__init__(maker, model, year, base_price, miles)
        
    def sale_price(self):
        s = 1.1
        return self.base_price * s
        
    def purchase_price(self):
        p = 0.009
        return self.sale_price() - (p * self.miles)
    
    def interest_rate(self):
        return 1.03

class Truck(Vehicle):
    def __init__(self, maker, model, year, base_price, miles):
        # Inherit vehicle attributes
        super(Truck, self).__init__(maker, model, year, base_price, miles)
        
    def sale_price(self):
        s = 1.6
        return self.base_price * s
        
    def purchase_price(self):
        p = 0.02
        return self.sale_price() - (p * self.miles)
        
    def interest_rate(self):
        return 1.11