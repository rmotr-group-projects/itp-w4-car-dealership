class Vehicle(object):
    def __init__(self, maker, model, year, base_price, miles=None):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        if not miles:
            self.miles = 0
        else:
            self.miles = miles

#Sale multipliers

#Car: 1.2
#Motorcycle: 1.1
#Truck: 1.6
#Purchase multipliers

#Car: 0.004
#Motorcycle: 0.009
#Truck: 0.02


class Car(Vehicle):
    S = 1.2
    P = 0.004
    I = 1.07
    
    def sale_price(self):
        self._sale_price = self.base_price * self.S
        return self._sale_price

    def purchase_price(self):
        self._purchase_price = self.sale_price() - (self.P * self.miles)
        return self._purchase_price

class Motorcycle(Vehicle):
    S = 1.1
    P = 0.009
    I = 1.03
    
    def sale_price(self):
        self._sale_price = self.base_price * self.S
        return self._sale_price

    def purchase_price(self):
        self._purchase_price = self.sale_price() - (self.P * self.miles)
        return self._purchase_price

class Truck(Vehicle):
    S = 1.6
    P = 0.02
    I = 1.11
    
    def sale_price(self):
        self._sale_price = self.base_price * self.S
        return self._sale_price

    def purchase_price(self):
        self._purchase_price = self.sale_price() - (self.P * self.miles)
        return self._purchase_price