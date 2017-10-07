class Vehicle(object):
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles

    def sale_price(self):
        raise NotImplementedError()
        
    def purchase_price(self):
        raise NotImplementedError()

class Car(Vehicle):
    
    INTEREST = 1.07
    SALE_MULTIPLIER = 1.2
    PURCHASE_MULTIPLIER = 0.004
    
    def sale_price(self):
        return self.base_price * 1.2
        
    def purchase_price(self):
        return self.sale_price() - (self.PURCHASE_MULTIPLIER * self.miles)


class Motorcycle(Vehicle):
    
    INTEREST = 1.03
    SALE_MULTIPLIER = 1
    PURCHASE_MULTIPLIER = 0.009
    
    def sale_price(self):
        return self.base_price * 1.1
        
    def purchase_price(self):
        return self.sale_price() - (self.PURCHASE_MULTIPLIER * self.miles)


class Truck(Vehicle):
    
    INTEREST = 1.11
    SALE_MULTIPLIER = 1.7
    PURCHASE_MULTIPLIER = 0.02
    
    def sale_price(self):
        return self.base_price * 1.6
        
    def purchase_price(self):
        return self.sale_price() - (self.PURCHASE_MULTIPLIER * self.miles)
