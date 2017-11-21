class Vehicle(object):
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.year = year
        self.base_price = base_price
        self.miles = miles
        self.model = model

class Car(Vehicle):
    def __init__(self, maker, model, year, base_price, miles):
        Vehicle.__init__(self, maker, model, year, base_price, miles)
    
    def sale_price(self):
        s = 1.2
        return self.base_price * s
        
    def purchase_price(self):
        p = 0.004 
        return self.sale_price() - (p * self.miles)
        
class Motorcycle(Vehicle):
    def __init__(self, maker, model, year, base_price, miles):
        Vehicle.__init__(self, maker, model, year, base_price, miles)
        
    def sale_price(self):
        s = 1.1
        return self.base_price * s
        
    def purchase_price(self):
        p = 0.009 
        return self.sale_price() - (p * self.miles)

class Truck(Vehicle):
    def __init__(self, maker, model, year, base_price, miles):
        Vehicle.__init__(self, maker, model, year, base_price, miles)
        
    def sale_price(self):
        s = 1.6
        return self.base_price * s

    def purchase_price(self):
        p = 0.02
        return self.sale_price() - (p * self.miles) 
        
        

