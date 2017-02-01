class Vehicle(object):
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles
        
    def sale_price(self):
        return self.base_price * self.sale_rate
        
    def purchase_price(self):
        return self.sale_price() - (self.purchase_rate * self.miles)
    

class Car(Vehicle):
    def __init__(self, maker, model, year, base_price, miles):
        super(Car,self).__init__(maker, model, year, base_price, miles)
        self.sale_rate = 1.2
        self.purchase_rate = 0.004  
        self.interest_rate = 1.07
        self.lease_rate = 1.2


class Motorcycle(Vehicle):
    def __init__(self, maker, model, year, base_price, miles):
        super(Motorcycle,self).__init__(maker, model, year, base_price, miles)
        self.sale_rate = 1.1 
        self.purchase_rate = 0.009 
        self.interest_rate = 1.03
        self.lease_rate = 1.0


class Truck(Vehicle):
    def __init__(self, maker, model, year, base_price, miles):
        super(Truck,self).__init__(maker, model, year, base_price, miles)
        self.sale_rate = 1.6 
        self.purchase_rate = 0.02 
        self.interest_rate = 1.11
        self.lease_rate = 1.7
