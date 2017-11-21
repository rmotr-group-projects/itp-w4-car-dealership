class Vehicle(object):
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker 
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles


class Car(Vehicle):
    def __init__(self, maker, model, year, base_price, miles):
        super(Car, self).__init__(maker, model, year, base_price, miles)
    
    def sale_price(self):
        return self.base_price * 1.2
    
    def purchase_price(self):
        return self.sale_price() - (0.004 * self.miles)
        
    def is_car(self):
        return True 
    def is_motorcycle(self):
        return False 
    def is_truck(self):
        return False 

class Motorcycle(Vehicle):
    def __init__(self, maker, model, year, base_price, miles):
        super(Motorcycle, self).__init__(maker, model, year, base_price, miles)
    
    def sale_price(self):
        return self.base_price * 1.1
    
    def purchase_price(self):
        return self.sale_price() - (0.009 * self.miles)
    
    def is_car(self):
        return False 
    def is_motorcycle(self):
        return True
    def is_truck(self):
        return False 


class Truck(Vehicle):
    def __init__(self, maker, model, year, base_price, miles):
        super(Truck, self).__init__(maker, model, year, base_price, miles)
    
    def sale_price(self):
        return self.base_price * 1.6
    
    def purchase_price(self):
        return self.sale_price() - (0.02 * self.miles)
    
    def is_car(self):
        return False 
    def is_motorcycle(self):
        return False 
    def is_truck(self):
        return True 