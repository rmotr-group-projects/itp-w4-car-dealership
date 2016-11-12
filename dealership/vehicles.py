class Vehicle(object):
    def __init__(self, maker, model, year, base_price, miles):
        self.maker=maker
        self.model=model
        self.year=year
        self.base_price=base_price
        self.miles=miles
        self.S = 1
        self.P = 1
    
    def sale_price(self):
        return self.S * self.base_price
    
    def purchase_price(self):
        return (self.sale_price() - (self.P * self.miles)) 

class Car(Vehicle):
    def __init__(self, maker, model, year, base_price, miles):
        #inherits the __init__ method to initialize attributes
        super(Car, self).__init__(maker, model, year, base_price, miles)
        self.S = 1.2
        self.P = 0.004
    
    def __repr__(self):
        return '<car:{}>'.format(self.maker)

class Motorcycle(Vehicle):
    def __init__(self, maker, model, year, base_price, miles):
        #inherits the __init__ method to initialize attributes
        super(Motorcycle, self).__init__(maker, model, year, base_price, miles)
        self.S = 1.1
        self.P = 0.009
    
    def __repr__(self):
        return '<moto:{}>'.format(self.maker)

class Truck(Vehicle):
    def __init__(self, maker, model, year, base_price, miles):
        #inherits the __init__ method to initialize attributes
        super(Truck, self).__init__(maker, model, year, base_price, miles)
        self.S = 1.6
        self.P = 0.02
    
    def __repr__(self):
        return '<truck:{}>'.format(self.maker)
