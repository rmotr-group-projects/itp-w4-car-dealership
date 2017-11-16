class Vehicle(object):
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles

        # variables initialized to make PyCharm happy
        self.sale_multiplier = 1
        self.purchase_multiplier = 1

    def sale_price(self):
        return self.base_price * self.sale_multiplier

    def purchase_price(self):
        return self.sale_price() - (self.purchase_multiplier * self.miles)


class Car(Vehicle):
    def __init__(self, maker, model, year, base_price, miles):
        super(Car, self).__init__(maker, model, year, base_price, miles)
        self.sale_multiplier = 1.2
        self.purchase_multiplier = 0.004


class Motorcycle(Vehicle):
    def __init__(self, maker, model, year, base_price, miles):
        super(Motorcycle, self).__init__(maker, model, year, base_price, miles)
        self.sale_multiplier = 1.1
        self.purchase_multiplier = 0.009


class Truck(Vehicle):
    def __init__(self, maker, model, year, base_price, miles):
        super(Truck, self).__init__(maker, model, year, base_price, miles)
        self.sale_multiplier = 1.6
        self.purchase_multiplier = 0.02
