class Vehicle(object):

    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles

    def sale_price(self):
        return self.base_price * self.get_sale_multiplier()

    def purchase_price(self):
        return self.sale_price() - (self.get_purchase_multiplier() * self.miles)


class Car(Vehicle):

    def __init__(self, maker, model, year, base_price, miles):
        Vehicle.__init__(self, maker, model, year, base_price, miles)

    def get_sale_multiplier(self):
        return 1.2

    def get_purchase_multiplier(self):
        return 0.004


class Motorcycle(Vehicle):

    def __init__(self, maker, model, year, base_price, miles):
        Motorcycle.__init__(self, maker, model, year, base_price, miles)

    def get_sale_multiplier(self):
        return 1.1

    def get_purchase_multiplier(self):
        return 0.009


class Truck(Vehicle):

    def __init__(self, maker, model, year, base_price, miles):
        Truck.__init__(self, maker, model, year, base_price, miles)



