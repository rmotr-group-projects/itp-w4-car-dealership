class Vehicle(object):
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles
        self.sale_multiplier = 1
        self.purchase_multiplier = 1
        self.interest_rate = 1

    def sale_price(self):
        return self.base_price * self.sale_multiplier

    def purchase_price(self):
        return self.sale_price() - (self.purchase_multiplier * self.miles)

    def lease_multiplier(self, length_in_months):
        raise NotImplementedError("lease_multiplier(length_in_months) not implemented")


class Car(Vehicle):
    def __init__(self, maker, model, year, base_price, miles):
        super(Car, self).__init__(maker, model, year, base_price, miles)
        self.sale_multiplier = 1.2
        self.purchase_multiplier = 0.004
        self.interest_rate = 1.07

    def lease_multiplier(self, length_in_months):
        return self.sale_price() * 1.2 / length_in_months if length_in_months != 0 else 0


class Motorcycle(Vehicle):
    def __init__(self, maker, model, year, base_price, miles):
        super(Motorcycle, self).__init__(maker, model, year, base_price, miles)
        self.sale_multiplier = 1.1
        self.purchase_multiplier = 0.009
        self.interest_rate = 1.03

    def lease_multiplier(self, length_in_months):
        return self.sale_price() / length_in_months if length_in_months != 0 else 0


class Truck(Vehicle):
    def __init__(self, maker, model, year, base_price, miles):
        super(Truck, self).__init__(maker, model, year, base_price, miles)
        self.sale_multiplier = 1.6
        self.purchase_multiplier = 0.02
        self.interest_rate = 1.11

    def lease_multiplier(self, length_in_months):
        return self.sale_price() * 1.7 / length_in_months if length_in_months != 0 else 0
