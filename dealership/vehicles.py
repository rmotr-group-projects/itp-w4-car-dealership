class Vehicle(object):
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles
        
    def sale_price(self):
        return self.base_price*self.get_sale_multiplier()
        
    def purchase_price(self):
        return self.sale_price() - (self.get_purchase_multiplier() * self.miles) 
    
    def get_sale_multiplier(self):
        raise NotImplementedError()
        
    def get_purchase_multiplier(self):
        raise NotImplementedError()
        
    def get_buy_multiplier(self):
        raise NotImplementedError()
        
    def get_lease_multiplier(self):
        raise NotImplementedError()

class Car(Vehicle):
    
    def get_sale_multiplier(self):
        return 1.2
    
    def get_purchase_multiplier(self):
        return 0.004
        
    def get_buy_multiplier(self):
        return 1.07

    def get_lease_multiplier(self):
        return 1.2

class Motorcycle(Vehicle):
    
    def get_sale_multiplier(self):
        return 1.1
    
    def get_purchase_multiplier(self):
        return 0.009
        
    def get_buy_multiplier(self):
        return 1.03

    def get_lease_multiplier(self):
        return 1

class Truck(Vehicle):
    
    def get_sale_multiplier(self):
        return 1.6
    
    def get_purchase_multiplier(self):
        return 0.02
        
    def get_buy_multiplier(self):
        return 1.11

    def get_lease_multiplier(self):
        return 1.7
