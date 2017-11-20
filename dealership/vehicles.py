class Vehicle(object):

    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles


class Car(Vehicle):

    def __init__(self, maker, model, year, base_price, miles):

        Vehicle.__init__(self, maker, model, year, base_price, miles)

    def sale_price(self):

        return self.base_price * 1.2


# STOPEED HERE, implement purchase price for others and test
    def purchase_price(self):
        """The price the dealership will pay a customer to buy her/his vehicle"""

        return self.sale_price() - (0.004 * self.miles)





class Motorcycle(Vehicle):

    def __init__(self, maker, model, year, base_price, miles):

        Motorcycle.__init__(self, maker, model, year, base_price, miles)

    def sale_price(self):

        return self.base_price * 1.1


class Truck(Vehicle):

    def __init__(self, maker, model, year, base_price, miles):

        Truck.__init__(self, maker, model, year, base_price, miles)

    def sale_price(self):

        return self.base_price * 1.6

