class Vehicle(object):
    SaleMultiplier = None
    PurchaseMultiplier = None

    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles

    def sale_price(self):
        return self.base_price * self.SaleMultiplier #access class attribute in instance method using self.__class__.attributename

    def purchase_price(self):
        return self.sale_price() - (self.PurchaseMultiplier * self.miles)


class Car(Vehicle):
    SaleMultiplier = 1.2
    PurchaseMultiplier = 0.004
    InterestRate = 1.07

    def lease_multiplier(self,length_in_months):
        return self.sale_price() * 1.2/length_in_months


class Motorcycle(Vehicle):
    SaleMultiplier = 1.1
    PurchaseMultiplier = 0.009
    InterestRate = 1.03

    def lease_multiplier(self,length_in_months):
        return self.sale_price() * 1/length_in_months


class Truck(Vehicle):
    SaleMultiplier = 1.6
    PurchaseMultiplier = 0.02
    InterestRate = 1.11

    def lease_multiplier(self, length_in_months):
        return self.sale_price() * 1.7/length_in_months



