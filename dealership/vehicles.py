class Vehicle(object):
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles        
        
    def sale_price(self):
        return self.base_price * self.S #S is a multiplier that will vary depending on the type of vehicle
    
    def purchase_price(self):
        return self.sale_price() - (self.P * self.miles) #P will be a multiplier depending on the type of vehicle
        
        

class Car(Vehicle):
    def __init__(self, maker, model, year, base_price, miles):
        super(Car,self).__init__(maker, model, year, base_price, miles)
        self.S = 1.2
        self.P = 0.004
        self.I = 1.07
        self.lease_multiplier = 1.2
        


class Motorcycle(Vehicle):
     def __init__(self, maker, model, year, base_price, miles):
        super(Motorcycle,self).__init__(maker, model, year, base_price, miles)
        self.S = 1.1
        self.P = 0.009
        self.I = 1.03
        self.lease_multiplier= 1


class Truck(Vehicle):
    def __init__(self, maker, model, year, base_price, miles):
        super(Truck,self).__init__(maker, model, year, base_price, miles)
        self.S = 1.6
        self.P = 0.02
        self.I = 1.11
        self.lease_multiplier= 1.7
