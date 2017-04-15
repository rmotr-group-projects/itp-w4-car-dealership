class Vehicle(object):
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles


class Car(Vehicle):
    def sale_price(self):
        return self.base_price * 1.2
    def purchase_price(self):
        return self.sale_price() - self.miles * .004

class Motorcycle(Vehicle):
    def sale_price(self):
        return self.base_price * 1.1
    def purchase_price(self):
        return self.sale_price() - self.miles * .009

class Truck(Vehicle):
    def sale_price(self):
        return self.base_price * 1.6
    def purchase_price(self):
        return self.sale_price() - self.miles * .02