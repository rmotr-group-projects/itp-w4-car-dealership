class Vehicle(object):
    def __init__(self, maker, model, year, base_price, miles):
        self.make = maker
        self.year = year
        self.price = base_price
        self.miles = miles
        
    def sale_price(self, m):
        return self.price * m
        
    def purchase_price(self, p):
        return sale_price() - (p * miles)

class Car(Vehicle):
    def __init__(self, maker, model, year, base_price, miles):
        Vehicle.__init__(self, maker, model, year, base_price, miles)
    
    def sale_price(self):
        s = 1.2
        return self.price * s
        
    def purchase_price(self, sale_price):
        p = 0.004 
        return self.sale_price() - (p * self.miles)
        
class Motorcycle(Vehicle):
    def __init__(self, maker, model, year, base_price, miles):
        Vehicle.__init__(self, maker, model, year, base_price, miles)
        
    def sale_price(self):
        s = 1.1
        return self.price * s
        
    def purchase_price(self, sale_price):
        p = 0.009 
        return self.sale_price() - (p * self.miles)

class Truck(Vehicle):
    def __init__(self, maker, model, year, base_price, miles):
        Vehicle.__init__(self, maker, model, year, base_price, miles)
        
    def sale_price(self):
        s = 1.6
        return self.price * s
        
        

