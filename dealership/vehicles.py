class Vehicle(object): #abstract class for the different vehicle types
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles

    def sale_price(self):
        return self.base_price * self.SaleMultiplier

    def purchase_price(self):
        return self.sale_price() - (self.PurchaseMultiplier * self.miles)

    def lease_multiplier(self, length_in_months):
        return self.sale_price() * self.VehicleMultiplier/length_in_months


class Car(Vehicle):
    SaleMultiplier = 1.2
    PurchaseMultiplier = 0.004
    InterestRate = 1.07
    VehicleMultiplier = 1.2



class Motorcycle(Vehicle):
    SaleMultiplier = 1.1
    PurchaseMultiplier = 0.009
    InterestRate = 1.03
    VehicleMultiplier = 1




class Truck(Vehicle):
    SaleMultiplier = 1.6
    PurchaseMultiplier = 0.02
    InterestRate = 1.11
    VehicleMultiplier = 1.7





