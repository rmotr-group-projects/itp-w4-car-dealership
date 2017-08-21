class Vehicle(object):
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles

#sale price = base_price * S 
#S = sale multiplier
#Car: 1.2
#Motorcycle: 1.1
#Truck: 1.6

#purchase price = sale_price() - (P * miles)
#P = price multiplier
#Car: 0.004
#Motorcycle: 0.009
#Truck: 0.02


class Car(Vehicle):
    def sale_price(self):
        return self.base_price * 1.2
    def purchase_price(self):
        return (self.sale_price() - (0.004 * self.miles))


class Motorcycle(Vehicle):
    def sale_price(self):
        return self.base_price * 1.1
    def purchase_price(self):
        return (self.sale_price() - (0.009 * self.miles))


class Truck(Vehicle):
    def sale_price(self):
        return self.base_price * 1.6
    def purchase_price(self):
        return (self.sale_price() - (0.02 * self.miles))
