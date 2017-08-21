class Vehicle(object):
    SALE_MULTIPLIER = 1
    PURCHASE_MULTIPLER = 1
    
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles

    def sale_price(self):
        return self.base_price * self.SALE_MULTIPLIER
        
    def purchase_price(self):
        return self.sale_price() - (self.PURCHASE_MULTIPLER * self.miles)
    
class Car(Vehicle):
    SALE_MULTIPLIER = 1.2
    PURCHASE_MULTIPLER = .004
    
class Motorcycle(Vehicle):
    SALE_MULTIPLIER = 1.1
    PURCHASE_MULTIPLER = .009


class Truck(Vehicle):
    SALE_MULTIPLIER = 1.6
    PURCHASE_MULTIPLER = .02


#PYTHONPATH=. py.test tests/test_vehicles.py::CarTestCase::test_sale_price