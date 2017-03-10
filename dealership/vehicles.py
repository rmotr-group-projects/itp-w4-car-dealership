class Vehicle(object):
    sales_multi = 1
    purchase_multi = 1
    
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles
        
    def sale_price(self):
        return self.base_price * self.sales_multi
        
    def purchase_price(self):
        return self.sale_price() - (self.purchase_multi * self.miles)


class Car(Vehicle):
    sales_multi = 1.2
    purchase_multi = 0.004
    interest_multi = 1.07
    lease_multi = 1.2


class Motorcycle(Vehicle):
    sales_multi = 1.1
    purchase_multi = 0.009
    interest_multi = 1.03
    lease_multi = 1


class Truck(Vehicle):
    sales_multi = 1.6
    purchase_multi = 0.02
    interest_multi = 1.11
    lease_multi = 1.7
