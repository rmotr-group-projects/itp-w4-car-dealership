class Vehicle(object):
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles


class Car(Vehicle):
    def purchase_price(self):
        return self.sale_price() - (.004 * self.miles)
    def sale_price(self):
        return self.base_price * 1.2
    

class Motorcycle(Vehicle):
    def purchase_price(self):
        return self.sale_price() - (.009 * self.miles)
    def sale_price(self):
        return self.base_price * 1.1
    


class Truck(Vehicle):
    def purchase_price(self):
        return self.sale_price() - (.02 * self.miles)
    def sale_price(self):
        return self.base_price * 1.6
   