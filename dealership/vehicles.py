class Vehicle(object):
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles
    
    def sale_price(self):
        return self.base_price * self.sales_modifier
    def purchase_price(self):
        return self.sale_price() - (self.P * self.miles)
    
            
class Car(Vehicle):
    sales_modifier = 1.2
    P =0.004
    I = 1.07
    #`sale_price() + (sale_price() * 1.2 / length_in_months)`
    L = 1.2

class Motorcycle(Vehicle):
    sales_modifier = 1.1
    P =0.009
    I = 1.03
    L = 1
## `sale_price() + (sale_price() * 1 / length_in_months)`
class Truck(Vehicle):
    sales_modifier = 1.6
    P = 0.02
    I = 1.11
    L = 1.7
## `sale_price() + (sale_price() * 1.7 / length_in_months)`    