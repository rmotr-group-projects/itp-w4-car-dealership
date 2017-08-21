class Vehicle(object):
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles


class Car(Vehicle):
    
    def sale_price(self):
        #formula base_price * s
        return (self.base_price * 1.2)
        
    def purchase_price(self):
        return (self.sale_price() - (0.004 * self.miles))


class Motorcycle(Vehicle):
    
    def sale_price(self):
        #formula base_price * s
        return (self.base_price * 1.1)
        
    def purchase_price(self):
        return (self.sale_price() - (0.009 * self.miles))


class Truck(Vehicle):
     
    def sale_price(self):
        #formula
        return (self.base_price * 1.6)
    
    def purchase_price(self):
        return (self.sale_price() - (0.02 * self.miles))


#PYTHONPATH=. py.test tests/test_vehicles.py::CarTestCase::test_cars_purchase_price