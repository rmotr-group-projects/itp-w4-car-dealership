class Vehicle(object):
    """Base class for vehicles at the car dealership"""

    def __init__(self, maker, model, year, base_price, miles, S=None, P=None, I=None, L=None):
        """Gather all necessary information for a vehicle"""

        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles
        self.S = None
        self.P = None
        self.I = None
        self.L = None

    def sale_price(self):
        """We want to know how much to sell a vehicle for (to a customer)"""

        return self.base_price * self.S

    def purchase_price(self):
        """We want to know how much the dealership should pay for a vehicle"""

        return self.sale_price() - (self.P * self.miles)

    def lease_multiplier(self):
        """Different vehicles have different lease rates"""

        return self.sale_price() * self.L

    def interest_rate(self):
        """Different vehicles have different interest rates"""

        return self.I * self.sale_price()


class Car(Vehicle):
    """Inherits from Base class Vehicle"""

    def __init__(self, maker, model, year, base_price, miles):
        """Gather all necessary information for a car"""

        super(Car, self).__init__(maker, model, year, base_price, miles)
        self.S = 1.2
        self.P = 0.004
        self.I = 1.07
        self.L = 1.2


class Motorcycle(Vehicle):
    """Inherits from base class vehicle"""

    def __init__(self, maker, model, year, base_price, miles):
        """Gather all necessary information for a motorcycle"""

        super(Motorcycle, self).__init__(maker, model, year, base_price, miles)
        self.S = 1.1
        self.P = 0.009
        self.I = 1.03
        self.L = 1


class Truck(Vehicle):
    """Inherits from base class vehicle"""

    def __init__(self, maker, model, year, base_price, miles):
        """Gather all necessary information for a truck"""

        super(Truck, self).__init__(maker, model, year, base_price, miles)
        self.S = 1.6
        self.P = 0.02
        self.I = 1.11
        self.L = 1.7
